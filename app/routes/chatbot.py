import os

from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from groq import Groq

from app.rag_utils import search_chunks

# =====================================================
# Blueprint
# =====================================================
chatbot_bp = Blueprint(
    "chatbot",
    __name__,
    url_prefix="/chatbot"
)

# =====================================================
# Groq Client
# =====================================================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in .env")

client = Groq(api_key=GROQ_API_KEY)

# =====================================================
# Notes Folder (Fallback)
# =====================================================
NOTES_FOLDER = "app/notes_data"
os.makedirs(NOTES_FOLDER, exist_ok=True)


# =====================================================
# Chatbot Page
# URL: /chatbot
# Endpoint: chatbot.chatbot_page
# =====================================================
@chatbot_bp.route("/", methods=["GET"])
@login_required
def chatbot_page():
    return render_template("chatbot.html")


# =====================================================
# Chat API
# URL: /chatbot/chat
# =====================================================
@chatbot_bp.route("/chat", methods=["POST"])
@login_required
def chat():

    try:

        data = request.get_json(silent=True)

        if not data:
            return jsonify({"error": "Invalid request"}), 400

        user_message = data.get("message", "").strip()

        if user_message == "":
            return jsonify({"error": "Message cannot be empty"}), 400

        # Short topic handling
        if len(user_message.split()) <= 5:
            user_message = f"Explain this topic clearly: {user_message}"

        # -----------------------------------------
        # RAG Search
        # -----------------------------------------
        relevant_notes = search_chunks(
            user_message,
            current_user.id
        )

        # -----------------------------------------
        # Fallback to extracted text file
        # -----------------------------------------
        if not relevant_notes:

            note_file = os.path.join(
                NOTES_FOLDER,
                f"{current_user.id}.txt"
            )

            if os.path.exists(note_file):

                with open(
                    note_file,
                    "r",
                    encoding="utf-8"
                ) as f:

                    relevant_notes = f.read()[:2500]

        if not relevant_notes:
            relevant_notes = "No relevant study material available."

        # -----------------------------------------
        # Prompt
        # -----------------------------------------
        messages = [

            {
                "role": "system",
                "content":
                """
You are an AI Tutor.

Answer ONLY using the student's uploaded study material.

Rules:

- Answer in simple language.
- If the user asks a topic, explain it.
- If information is partial, answer with available information.
- If nothing is found, say:
"Sorry, this topic is not available in your uploaded notes."
"""
            },

            {
                "role": "user",
                "content":
f"""
Study Material:

{relevant_notes}


Question:

{user_message}
"""
            }

        ]

        # -----------------------------------------
        # Groq
        # -----------------------------------------
        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=messages,

            temperature=0.4,

            max_tokens=500

        )

        answer = response.choices[0].message.content.strip()

        print("=" * 70)
        print("USER :", user_message)
        print("=" * 70)
        print("NOTES :", relevant_notes[:300])
        print("=" * 70)
        print("AI :", answer)
        print("=" * 70)

        return jsonify({
            "reply": answer
        })

    except Exception as e:

        print("CHATBOT ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 500