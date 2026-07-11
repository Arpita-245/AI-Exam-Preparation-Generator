from io import BytesIO

from flask import Blueprint
from flask import send_file

from flask_login import login_required
from flask_login import current_user

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from app.models import StudyMaterial
from app.models import QuizResult


pdf_bp = Blueprint("pdf", __name__)


# ==========================================================
# Download Summary PDF
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

    story.append(
        Paragraph(
            "<b>AI-Based Exam Preparation System</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            "<b>AI Generated Summary</b>",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Study Material:</b> {note.original_filename}",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            note.summary.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    doc.build(story)

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="Summary.pdf",
        mimetype="application/pdf"
    )


# ==========================================================
# Download Quiz Result PDF
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

    story.append(
        Paragraph(
            "<b>AI-Based Exam Preparation System</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            "<b>Quiz Performance Report</b>",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Study Material:</b> {note.original_filename}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Score:</b> {result.score}/{result.total_questions}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Percentage:</b> {result.percentage}%",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Attempt Date:</b> {result.attempted_on.strftime('%d-%m-%Y %H:%M')}",
            styles["BodyText"]
        )
    )

    # AI Feedback

    if result.percentage >= 80:

        feedback = (
            "Excellent performance! You have a strong understanding "
            "of the study material. Keep practicing to maintain "
            "your performance."
        )

    elif result.percentage >= 50:

        feedback = (
            "Good job! Your understanding is satisfactory, but "
            "revising difficult topics and solving more quizzes "
            "will improve your score."
        )

    else:

        feedback = (
            "Your score indicates that you should revisit the summary, "
            "study the concepts again, and practice more questions."
        )

    story.append(
        Paragraph(
            "<b>AI Feedback</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            feedback,
            styles["BodyText"]
        )
    )

    doc.build(story)

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="Quiz_Result.pdf",
        mimetype="application/pdf"
    )


# ==========================================================
# Download Recommendation PDF
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

    story.append(
        Paragraph(
            "<b>AI-Based Exam Preparation System</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            "<b>Personalized Study Recommendation</b>",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Study Material:</b> {note.original_filename}",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            note.recommendation.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    doc.build(story)

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="Study_Recommendation.pdf",
        mimetype="application/pdf"
    )