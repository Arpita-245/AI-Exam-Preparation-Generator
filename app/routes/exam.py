from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import login_required, current_user

from app.extensions import db
from app.models import StudyMaterial, QuizResult
from app.services.quiz_parser import QuizParser

exam_bp = Blueprint("exam", __name__)


# ==================================================
# Attempt Quiz
# ==================================================

@exam_bp.route("/attempt-quiz/<int:note_id>")
@login_required
def attempt_quiz(note_id):

    note = StudyMaterial.query.get_or_404(note_id)

    # Security
    if note.user_id != current_user.id:
        flash("Unauthorized access.", "danger")
        return redirect(url_for("notes.my_notes"))

    if not note.quiz:
        flash("Quiz has not been generated yet.", "warning")
        return redirect(url_for("notes.my_notes"))

    questions = QuizParser.parse(note.quiz)

    if not questions:
        flash("Unable to read the quiz.", "danger")
        return redirect(url_for("quiz.view_quiz", note_id=note.id))

    return render_template(
        "attempt_quiz.html",
        note=note,
        questions=questions
    )


# ==================================================
# Submit Quiz
# ==================================================

@exam_bp.route("/submit-quiz/<int:note_id>", methods=["POST"])
@login_required
def submit_quiz(note_id):

    note = StudyMaterial.query.get_or_404(note_id)

    # Security
    if note.user_id != current_user.id:
        flash("Unauthorized access.", "danger")
        return redirect(url_for("notes.my_notes"))

    questions = QuizParser.parse(note.quiz)

    if not questions:
        flash("Quiz data is invalid.", "danger")
        return redirect(url_for("notes.my_notes"))

    score = 0
    total = len(questions)

    for i, question in enumerate(questions, start=1):

        student_answer = request.form.get(f"q{i}")
        correct_answer = question["answer"]

        if student_answer == correct_answer:
            score += 1

    percentage = round((score / total) * 100, 2) if total > 0 else 0

    try:
        # Save quiz result
        result = QuizResult(
            score=score,
            total_questions=total,
            percentage=percentage,
            study_material_id=note.id,
            user_id=current_user.id
        )

        db.session.add(result)

        # Allow recommendation to be regenerated
        note.recommendation_generated = False

        db.session.commit()

        flash(
            f"Quiz submitted successfully! Score: {score}/{total} ({percentage}%)",
            "success"
        )

    except Exception as e:
        db.session.rollback()
        print("QUIZ SUBMISSION ERROR:", e)

        flash(f"Error saving quiz result: {str(e)}", "danger")

    return redirect(url_for("dashboard.dashboard"))