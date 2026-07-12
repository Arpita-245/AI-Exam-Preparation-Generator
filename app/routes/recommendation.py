from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required
from flask_login import current_user

from app.extensions import db
from app.models import StudyMaterial
from app.models import QuizResult

from app.services.recommendation_service import RecommendationService

recommendation_bp = Blueprint("recommendation", __name__)


# ==========================================
# Generate Recommendation
# ==========================================

@recommendation_bp.route("/generate-recommendation/<int:note_id>")
@login_required
def generate_recommendation(note_id):

    note = StudyMaterial.query.get_or_404(note_id)

    # Check whether summary exists
    if not note.summary_generated or not note.summary:
        flash("Please generate the summary first.", "error")
        return redirect(url_for("notes.my_notes"))

    # Check whether recommendation already exists
    if note.recommendation_generated:
        flash("Recommendation already generated.", "success")
        return redirect(
            url_for("recommendation.view_recommendation", note_id=note.id)
        )

    # Get latest quiz result
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
        flash("Please attempt the quiz first.", "error")
        return redirect(url_for("notes.my_notes"))

    # Generate recommendation using AI
    recommendation = RecommendationService.generate_recommendation(
        summary=note.summary,
        quiz_score=f"{latest_result.score}/{latest_result.total_questions}"
    )

    # Save recommendation
    note.recommendation = recommendation
    note.recommendation_generated = True

    db.session.commit()

    flash("Study Recommendation generated successfully!", "success")

    return redirect(
        url_for("recommendation.view_recommendation", note_id=note.id)
    )


# ==========================================
# View Recommendation
# ==========================================

@recommendation_bp.route("/recommendation/<int:note_id>")
@login_required
def view_recommendation(note_id):

    note = StudyMaterial.query.get_or_404(note_id)

    if not note.recommendation_generated:
        flash("Recommendation has not been generated yet.", "error")
        return redirect(url_for("notes.my_notes"))

    return render_template(
        "recommendation.html",
        note=note
    )