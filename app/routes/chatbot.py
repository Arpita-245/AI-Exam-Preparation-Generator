from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required, current_user
from groq import Groq
import os

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
# Notes Folder
# ==========================================
NOTES_FOLDER = "app/notes_data"

# Ensure folder exists
os.makedirs(NOTES_FOLDER, exist_ok=True)


# ==========================================
# ✅ UI ROUTE
# ==========================================
@chatbot_bp.route("/chatbot", methods=["GET"])
@login_required
def chatbot_page():
    return render_template("chatbot.html")


# ==========================================
# ✅ CHAT ROUTE (SAFE + OPTIMIZED)
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
        # ✅ LOAD USER NOTES FILE
        # ----------------------------------
        notes_file = os.path.join(NOTES_FOLDER, f"{current_user.id}.txt")

        notes = ""

        if os.path.exists(notes_file):
            try:
                with open(notes_file, "r", encoding="utf-8") as f:
                    notes = f.read()
            except Exception as e:
                print("❌ Error reading notes:", e)
                notes = ""

        # ----------------------------------
        # ✅ LIMIT SIZE (VERY IMPORTANT)
        # ----------------------------------
        notes = notes[:4000]  # Prevent token overflow

        # ----------------------------------
        # 🧠 PROMPT ENGINEERING
        # ----------------------------------
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an AI exam assistant.\n"
                    "Answer ONLY using the provided notes.\n"
                    "If the answer is not found in notes, reply exactly:\n"
                    "'Not in notes'"
                )
            },
            {
                "role": "user",
                "content": f"""
NOTES:
{notes}

QUESTION:
{user_message}
"""
            }
        ]

        # ----------------------------------
        # 🔥 CALL GROQ API (SAFE)
        # ----------------------------------
        response = client.chat.completions.create(
            messages=messages,
            model="llama-3.1-8b-instant",
            temperature=0.3,   # more accurate answers
            max_tokens=300     # prevent long responses
        )

        reply = (
            response.choices[0].message.content.strip()
            if response and response.choices
            else "No response"
        )

        # ----------------------------------
        # 🧾 LOGGING (SAFE)
        # ----------------------------------
        print(f"👤 User ({current_user.id}): {user_message}")
        print(f"🤖 AI: {reply}")

        return jsonify({"reply": reply})

    except Exception as e:
        print("❌ ERROR (CHAT):", str(e))
        return jsonify({"error": "Internal server error"}), 500