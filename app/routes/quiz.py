from flask import (
    Blueprint,
    redirect,
    render_template,
    flash,
    url_for
)

from flask_login import login_required

from app.extensions import db
from app.models import StudyMaterial
from app.services.quiz_service import QuizService

quiz_bp = Blueprint("quiz", __name__)


# ==========================================
# Generate Quiz
# ==========================================

@quiz_bp.route("/generate-quiz/<int:note_id>")
@login_required
def generate_quiz(note_id):

    note = StudyMaterial.query.get_or_404(note_id)

    # Check extracted text
    if not note.extracted_text:
        flash("No extracted text found.", "error")
        return redirect(url_for("notes.my_notes"))

    print("\n========== GENERATING QUIZ ==========")

    quiz = QuizService.generate_quiz(note.extracted_text)

    print("Generated Quiz:\n")
    print(quiz)

    # Save quiz
    note.quiz = quiz
    note.quiz_generated = True

    db.session.commit()

    print("\nQuiz saved successfully!")
    print("quiz_generated =", note.quiz_generated)
    print("=====================================\n")

    flash("Quiz generated successfully!", "success")

    return redirect(
        url_for(
            "quiz.view_quiz",
            note_id=note.id
        )
    )


# ==========================================
# View Quiz
# ==========================================

@quiz_bp.route("/quiz/<int:note_id>")
@login_required
def view_quiz(note_id):

    note = StudyMaterial.query.get_or_404(note_id)

    if not note.quiz:
        flash("Quiz has not been generated yet.", "error")
        return redirect(url_for("notes.my_notes"))

    return render_template(
        "quiz.html",
        note=note
    )