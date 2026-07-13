from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash
)

from flask_login import login_required, current_user

from app.extensions import db
from app.models import StudyMaterial, QuizResult
from app.services.recommendation_service import RecommendationService

import logging

recommendation_bp = Blueprint("recommendation", __name__)

logger = logging.getLogger(__name__)


# ==================================================
# Generate Recommendation
# ==================================================
@recommendation_bp.route("/generate-recommendation/<int:note_id>")
@login_required
def generate_recommendation(note_id):

    note = StudyMaterial.query.get_or_404(note_id)

    # Security Check
    if note.user_id != current_user.id:
        flash("Unauthorized access.", "danger")
        return redirect(url_for("notes.notes"))

    # Summary must exist
    if not note.summary_generated or not note.summary:
        flash("Please generate the summary first.", "warning")
        return redirect(url_for("notes.notes"))

    # Prevent duplicate generation
    if note.recommendation_generated:
        flash("Recommendation already generated.", "info")
        return redirect(
            url_for(
                "recommendation.view_recommendation",
                note_id=note.id
            )
        )

    # Latest quiz result
    latest_result = (
        QuizResult.query
        .filter_by(
            user_id=current_user.id,
            study_material_id=note.id
        )
        .order_by(QuizResult.attempted_on.desc())
        .first()
    )

    if latest_result is None:
        flash("Please attempt the quiz first.", "warning")
        return redirect(url_for("notes.notes"))

    try:

        recommendation = RecommendationService.generate_recommendation(
            summary=note.summary,
            quiz_score=f"{latest_result.score}/{latest_result.total_questions}"
        )

        if not recommendation:
            flash("Failed to generate recommendation.", "danger")
            return redirect(url_for("notes.notes"))

        # Save recommendation
        note.recommendation = recommendation
        note.recommendation_generated = True

        db.session.commit()

        flash("Study recommendation generated successfully!", "success")

        return redirect(
            url_for(
                "recommendation.view_recommendation",
                note_id=note.id
            )
        )

    except Exception as e:

        db.session.rollback()

        logger.error(f"RECOMMENDATION ERROR: {str(e)}")

        flash("Error generating recommendation.", "danger")

        return redirect(url_for("notes.notes"))


# ==================================================
# View Recommendation
# ==================================================
@recommendation_bp.route("/recommendation/<int:note_id>")
@login_required
def view_recommendation(note_id):

    note = StudyMaterial.query.get_or_404(note_id)

    # Security Check
    if note.user_id != current_user.id:
        flash("Unauthorized access.", "danger")
        return redirect(url_for("notes.notes"))

    if not note.recommendation_generated or not note.recommendation:
        flash("Recommendation has not been generated yet.", "warning")
        return redirect(url_for("notes.notes"))

    return render_template(
        "recommendation.html",
        note=note
    )