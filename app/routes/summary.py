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
from app.services.summary_service import SummaryService

summary_bp = Blueprint("summary", __name__)


# ==========================================
# Generate AI Summary
# ==========================================

@summary_bp.route("/generate-summary/<int:note_id>")
@login_required
def generate_summary(note_id):

    note = StudyMaterial.query.get_or_404(note_id)

    # Check if extracted text exists
    if not note.extracted_text:

        flash("No extracted text found.")

        return redirect(url_for("notes.my_notes"))

    # Generate summary using Gemini AI
    summary = SummaryService.generate_summary(
        note.extracted_text
    )

    # Save summary into database
    note.summary = summary

    note.summary_generated = True

    db.session.commit()

    return redirect(
        url_for(
            "summary.view_summary",
            note_id=note.id
        )
    )


# ==========================================
# View Summary
# ==========================================

@summary_bp.route("/summary/<int:note_id>")
@login_required
def view_summary(note_id):

    note = StudyMaterial.query.get_or_404(note_id)

    return render_template(
        "summary.html",
        note=note
    )