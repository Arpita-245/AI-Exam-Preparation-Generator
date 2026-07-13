from flask import (
    Blueprint,
    render_template,
    redirect,
    flash,
    url_for,
    request
)

from flask_login import login_required, current_user

from app.extensions import db
from app.models import StudyMaterial, QuizResult
from app.services.quiz_service import QuizService

import json
import logging

quiz_bp = Blueprint("quiz", __name__)

logger = logging.getLogger(__name__)


# ==================================================
# Generate Quiz
# ==================================================
@quiz_bp.route("/generate-quiz/<int:note_id>")
@login_required
def generate_quiz(note_id):

    note = StudyMaterial.query.get_or_404(note_id)

    if note.user_id != current_user.id:
        flash("Unauthorized access.", "danger")
        return redirect(url_for("notes.notes"))

    if not note.extracted_text:
        flash("No extracted text found.", "warning")
        return redirect(url_for("notes.notes"))

    try:

        quiz = QuizService.generate_quiz(
            note.extracted_text
        )

        if not quiz:
            flash("Quiz generation failed.", "danger")
            return redirect(url_for("notes.notes"))

        note.quiz = json.dumps(quiz)
        note.quiz_generated = True

        db.session.commit()

        flash("Quiz generated successfully!", "success")

        return redirect(
            url_for(
                "quiz.view_quiz",
                note_id=note.id
            )
        )

    except Exception as e:

        db.session.rollback()

        logger.error(
            f"QUIZ GENERATE ERROR: {str(e)}"
        )

        flash(
            "Error generating quiz.",
            "danger"
        )

        return redirect(url_for("notes.notes"))


# ==================================================
# View Quiz
# ==================================================
@quiz_bp.route("/quiz/<int:note_id>")
@login_required
def view_quiz(note_id):

    note = StudyMaterial.query.get_or_404(note_id)

    if note.user_id != current_user.id:
        flash("Unauthorized access.", "danger")
        return redirect(url_for("notes.notes"))

    if not note.quiz:
        flash("Quiz not generated yet.", "warning")
        return redirect(url_for("notes.notes"))

    try:

        quiz_data = json.loads(note.quiz)

    except Exception:

        flash("Invalid quiz data.", "danger")
        return redirect(url_for("notes.notes"))

    return render_template(
        "quiz.html",
        note=note,
        quiz=quiz_data
    )


# ==================================================
# Attempt Quiz
# ==================================================
@quiz_bp.route("/attempt-quiz/<int:note_id>")
@login_required
def attempt_quiz(note_id):

    note = StudyMaterial.query.get_or_404(note_id)

    if note.user_id != current_user.id:
        flash("Unauthorized access.", "danger")
        return redirect(url_for("notes.notes"))

    if not note.quiz:
        flash("Quiz not available.", "warning")
        return redirect(url_for("notes.notes"))

    try:

        quiz_data = json.loads(note.quiz)

    except Exception:

        flash("Invalid quiz data.", "danger")
        return redirect(url_for("notes.notes"))

    return render_template(
        "attempt_quiz.html",
        note=note,
        quiz=quiz_data
    )


# ==================================================
# Submit Quiz
# ==================================================
@quiz_bp.route(
    "/submit-quiz/<int:note_id>",
    methods=["POST"]
)
@login_required
def submit_quiz(note_id):

    note = StudyMaterial.query.get_or_404(note_id)

    if note.user_id != current_user.id:
        flash("Unauthorized access.", "danger")
        return redirect(url_for("notes.notes"))

    if not note.quiz:
        flash("Quiz not found.", "danger")
        return redirect(url_for("notes.notes"))

    try:

        quiz_data = json.loads(note.quiz)

        score = 0
        total_questions = len(quiz_data)

        for i, question in enumerate(quiz_data):

            selected_answer = request.form.get(
                f"q{i}"
            )

            correct_answer = question.get(
                "answer"
            )

            if selected_answer == correct_answer:
                score += 1

        percentage = 0

        if total_questions > 0:
            percentage = (
                score / total_questions
            ) * 100

        # =================================
        # Save Result
        # =================================
        result = QuizResult(
            user_id=current_user.id,
            study_material_id=note.id,
            score=score,
            total_questions=total_questions,
            percentage=percentage
        )

        db.session.add(result)
        db.session.commit()

        flash(
            f"Quiz submitted successfully! "
            f"Score: {score}/{total_questions} "
            f"({percentage:.1f}%)",
            "success"
        )

        return redirect(
            url_for("result.results")
        )

    except Exception as e:

        db.session.rollback()

        logger.error(
            f"QUIZ SUBMIT ERROR: {str(e)}"
        )

        flash(
            "Error submitting quiz.",
            "danger"
        )

        return redirect(url_for("notes.notes"))