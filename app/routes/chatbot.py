from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required

chatbot_bp = Blueprint("chatbot", __name__)


@chatbot_bp.route("/chatbot")
@login_required
def chatbot():
    return render_template("chatbot.html")


@chatbot_bp.route("/ask", methods=["POST"])
@login_required
def ask():

    user_message = request.json.get("message")

    # 🔥 SIMPLE AI LOGIC (you can upgrade later)
    if "study" in user_message.lower():
        reply = "You should revise daily and take quizzes regularly."
    elif "score" in user_message.lower():
        reply = "Focus on weak topics and practice more questions."
    else:
        reply = "I'm your AI assistant. Ask me about studies!"

    return jsonify({"reply": reply})