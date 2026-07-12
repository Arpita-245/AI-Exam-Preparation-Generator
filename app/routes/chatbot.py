from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required, current_user
from groq import Groq
import os

# ✅ NEW (RAG IMPORT)
from app.rag_utils import search_chunks

# ==========================================
# Create Blueprint
# ==========================================
chatbot_bp = Blueprint("chatbot", __name__)

# ==========================================
# Initialize Groq Client
# ==========================================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY is not set")

client = Groq(api_key=GROQ_API_KEY)

# ==========================================
# Notes Folder (fallback only)
# ==========================================
NOTES_FOLDER = "app/notes_data"
os.makedirs(NOTES_FOLDER, exist_ok=True)


# ==========================================
# ✅ UI ROUTE
# ==========================================
@chatbot_bp.route("/chatbot", methods=["GET"])
@login_required
def chatbot_page():
    return render_template("chatbot.html")


# ==========================================
# ✅ CHAT ROUTE (RAG VERSION 🚀)
# ==========================================
@chatbot_bp.route("/chat", methods=["POST"])
@login_required
def chat():
    try:
        # ----------------------------------
        # ✅ SAFE JSON PARSING
        # ----------------------------------
        data = request.get_json(silent=True)

        if not data:
            return jsonify({"error": "Invalid JSON request"}), 400

        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400

        # ----------------------------------
        # 🧠 SEMANTIC SEARCH (🔥 MAIN UPGRADE)
        # ----------------------------------
        relevant_notes = search_chunks(user_message, current_user.id)

        # Fallback if no index exists yet
        if not relevant_notes:
            print("⚠️ No RAG data found, using fallback notes")

            notes_file = os.path.join(NOTES_FOLDER, f"{current_user.id}.txt")
            relevant_notes = ""

            if os.path.exists(notes_file):
                with open(notes_file, "r", encoding="utf-8") as f:
                    relevant_notes = f.read()[:2000]

        if not relevant_notes:
            relevant_notes = "No relevant notes found."

        # ----------------------------------
        # 🧠 PROMPT ENGINEERING (UPDATED)
        # ----------------------------------
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an AI exam assistant.\n"
                    "Answer ONLY using the provided notes.\n"
                    "If not found, reply exactly: 'Not in notes'"
                )
            },
            {
                "role": "user",
                "content": f"""
NOTES:
{relevant_notes}

QUESTION:
{user_message}
"""
            }
        ]

        # ----------------------------------
        # 🔥 CALL GROQ API
        # ----------------------------------
        response = client.chat.completions.create(
            messages=messages,
            model="llama-3.1-8b-instant",
            temperature=0.3,
            max_tokens=300
        )

        reply = (
            response.choices[0].message.content.strip()
            if response and response.choices
            else "No response"
        )

        # ----------------------------------
        # 🧾 LOGGING
        # ----------------------------------
        print(f"👤 User ({current_user.id}): {user_message}")
        print(f"📚 Retrieved Notes: {relevant_notes[:200]}...")
        print(f"🤖 AI: {reply}")

        return jsonify({"reply": reply})

    except Exception as e:
        print("❌ ERROR (CHAT):", str(e))
        return jsonify({"error": "Internal server error"}), 500