from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required, current_user
from groq import Groq
import os

from app.rag_utils import search_chunks

# ==========================================
# ✅ CREATE BLUEPRINT
# ==========================================
chatbot_bp = Blueprint("chatbot", __name__)

# ==========================================
# 🔑 API KEY
# ==========================================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY is not set")

client = Groq(api_key=GROQ_API_KEY)

# ==========================================
# 📁 NOTES FOLDER (fallback)
# ==========================================
NOTES_FOLDER = "app/notes_data"
os.makedirs(NOTES_FOLDER, exist_ok=True)

# ==========================================
# ✅ UI ROUTE (IMPORTANT - YOU WERE MISSING THIS)
# ==========================================
@chatbot_bp.route("/", methods=["GET"])
@login_required
def chatbot_page():
    return render_template("chatbot.html")


# ==========================================
# 🤖 CHAT ROUTE (RAG + FIXED PROMPT)
# ==========================================
@chatbot_bp.route("/chat", methods=["POST"])
@login_required
def chat():
    try:
        # ----------------------------------
        # ✅ SAFE JSON
        # ----------------------------------
        data = request.get_json(silent=True)

        if not data:
            return jsonify({"error": "Invalid JSON request"}), 400

        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400

        # ----------------------------------
        # 🔥 FIX 1: HANDLE SHORT QUERIES (HEADINGS)
        # ----------------------------------
        if len(user_message.split()) <= 5:
            user_message = "Explain this topic clearly: " + user_message

        # ----------------------------------
        # 🧠 RAG SEARCH
        # ----------------------------------
        relevant_notes = search_chunks(user_message, current_user.id)

        # ----------------------------------
        # 📄 FALLBACK (if no embeddings)
        # ----------------------------------
        if not relevant_notes:
            print("⚠️ No RAG results, using fallback file")

            notes_file = os.path.join(NOTES_FOLDER, f"{current_user.id}.txt")

            if os.path.exists(notes_file):
                with open(notes_file, "r", encoding="utf-8") as f:
                    relevant_notes = f.read()[:2000]

        if not relevant_notes:
            relevant_notes = "No relevant notes found."

        # ----------------------------------
        # 🔥 FIX 2: SMART PROMPT
        # ----------------------------------
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a helpful AI exam assistant.\n\n"
                    "Rules:\n"
                    "- Answer using the provided notes.\n"
                    "- Try even if partial information exists.\n"
                    "- If question is a topic or heading, explain it clearly.\n"
                    "- Do NOT require exact match.\n"
                    "- Only say 'Not in notes' if nothing is relevant.\n"
                    "- Keep answers simple and clear."
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
        # 🤖 GROQ CALL
        # ----------------------------------
        response = client.chat.completions.create(
            messages=messages,
            model="llama-3.1-8b-instant",
            temperature=0.4,
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