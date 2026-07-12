from io import BytesIO
import os

from flask import Blueprint, send_file, request, jsonify
from flask_login import login_required, current_user

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader

from config import Config
from app.models import StudyMaterial, QuizResult


pdf_bp = Blueprint("pdf", __name__)

# ==========================================================
# 📂 Folder for storing extracted notes
# ==========================================================
NOTES_FOLDER = "app/notes_data"

# ✅ Fix Windows file/folder conflict
if os.path.exists(NOTES_FOLDER) and not os.path.isdir(NOTES_FOLDER):
    os.remove(NOTES_FOLDER)

os.makedirs(NOTES_FOLDER, exist_ok=True)


# ==========================================================
# 📄 Extract text from PDF
# ==========================================================
def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        try:
            text += page.extract_text() or ""
        except:
            pass  # skip problematic pages safely

    return text


# ==========================================================
# 📥 Load notes for chatbot (NEW - IMPORTANT)
# ==========================================================
def load_user_notes(user_id):
    path = os.path.join(NOTES_FOLDER, f"{user_id}.txt")

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    return ""


# ==========================================================
# 🚀 Upload PDF + Save Notes (FIXED)
# ==========================================================
@pdf_bp.route("/upload-pdf", methods=["POST"])
@login_required
def upload_pdf():

    # ✅ Check file exists
    if "pdf" not in request.files:
        return jsonify({"error": "No file part in request"}), 400

    file = request.files["pdf"]

    # ✅ Check filename
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Save PDF
    filename = secure_filename(file.filename)
    filepath = os.path.join(Config.UPLOAD_FOLDER, filename)

    os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
    file.save(filepath)

    # Extract text
    extracted_text = extract_text(filepath)

    # ✅ Handle empty extraction
    if not extracted_text.strip():
        return jsonify({"error": "Could not extract text from PDF"}), 400

    # Save notes to file
    notes_file = os.path.join(NOTES_FOLDER, f"{current_user.id}.txt")

    with open(notes_file, "w", encoding="utf-8") as f:
        f.write(extracted_text)

    print(f"✅ PDF processed & notes saved for user {current_user.id}")

    return jsonify({
        "message": "PDF uploaded and processed successfully",
        "text_preview": extracted_text[:300]  # helpful debug
    })


# ==========================================================
# 📄 Download Summary PDF
# ==========================================================
@pdf_bp.route("/download-summary/<int:note_id>")
@login_required
def download_summary(note_id):

    note = StudyMaterial.query.get_or_404(note_id)

    if note.user_id != current_user.id:
        return "Unauthorized", 403

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>AI-Based Exam Preparation System</b>", styles["Title"]))
    story.append(Paragraph("<b>AI Generated Summary</b>", styles["Heading1"]))
    story.append(Paragraph(f"<b>Study Material:</b> {note.original_filename}", styles["Heading2"]))
    story.append(Paragraph(note.summary.replace("\n", "<br/>"), styles["BodyText"]))

    doc.build(story)
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name="Summary.pdf", mimetype="application/pdf")


# ==========================================================
# 📊 Download Quiz Result PDF
# ==========================================================
@pdf_bp.route("/download-result/<int:result_id>")
@login_required
def download_result(result_id):

    result = QuizResult.query.get_or_404(result_id)

    if result.user_id != current_user.id:
        return "Unauthorized", 403

    note = StudyMaterial.query.get(result.study_material_id)

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>AI-Based Exam Preparation System</b>", styles["Title"]))
    story.append(Paragraph("<b>Quiz Performance Report</b>", styles["Heading1"]))
    story.append(Paragraph(f"<b>Study Material:</b> {note.original_filename}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Score:</b> {result.score}/{result.total_questions}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Percentage:</b> {result.percentage}%", styles["BodyText"]))
    story.append(Paragraph(f"<b>Attempt Date:</b> {result.attempted_on.strftime('%d-%m-%Y %H:%M')}", styles["BodyText"]))

    # AI Feedback
    if result.percentage >= 80:
        feedback = "Excellent performance! Keep it up."
    elif result.percentage >= 50:
        feedback = "Good job! Revise more for better results."
    else:
        feedback = "You should revisit concepts and practice more."

    story.append(Paragraph("<b>AI Feedback</b>", styles["Heading2"]))
    story.append(Paragraph(feedback, styles["BodyText"]))

    doc.build(story)
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name="Quiz_Result.pdf", mimetype="application/pdf")


# ==========================================================
# 📘 Download Recommendation PDF
# ==========================================================
@pdf_bp.route("/download-recommendation/<int:note_id>")
@login_required
def download_recommendation(note_id):

    note = StudyMaterial.query.get_or_404(note_id)

    if note.user_id != current_user.id:
        return "Unauthorized", 403

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>AI-Based Exam Preparation System</b>", styles["Title"]))
    story.append(Paragraph("<b>Personalized Study Recommendation</b>", styles["Heading1"]))
    story.append(Paragraph(f"<b>Study Material:</b> {note.original_filename}", styles["Heading2"]))
    story.append(Paragraph(note.recommendation.replace("\n", "<br/>"), styles["BodyText"]))

    doc.build(story)
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name="Study_Recommendation.pdf", mimetype="application/pdf")