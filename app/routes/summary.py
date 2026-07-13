import logging

from flask import (
    Blueprint,
    render_template,
    redirect,
    flash,
    url_for
)

from flask_login import (
    login_required,
    current_user
)

from app.extensions import db
from app.models import StudyMaterial
from app.services.summary_service import SummaryService

# ==========================================================
# Blueprint
# ==========================================================
summary_bp = Blueprint("summary", __name__)

logger = logging.getLogger(__name__)


# ==========================================================
# Generate AI Summary
# ==========================================================
@summary_bp.route("/generate-summary/<int:note_id>")
@login_required
def generate_summary(note_id):

    try:

        note = db.session.get(StudyMaterial, note_id)

        if note is None:
            flash("Study material not found.", "danger")
            return redirect(url_for("notes.notes"))

        # Security Check
        if note.user_id != current_user.id:
            flash("Unauthorized access.", "danger")
            return redirect(url_for("notes.notes"))

        # Already Generated
        if note.summary_generated and note.summary:
            flash("Summary already exists.", "info")
            return redirect(
                url_for(
                    "summary.view_summary",
                    note_id=note.id
                )
            )

        # No extracted text
        if not note.extracted_text or not note.extracted_text.strip():
            flash(
                "No extracted text found. Upload a valid document first.",
                "warning"
            )
            return redirect(url_for("notes.notes"))

        # Generate Summary
        summary = SummaryService.generate_summary(
            note.extracted_text
        )

        if not summary:
            flash(
                "AI could not generate a summary.",
                "danger"
            )
            return redirect(url_for("notes.notes"))

        # Save
        note.summary = summary
        note.summary_generated = True

        db.session.commit()

        flash(
            "Summary generated successfully!",
            "success"
        )

        return redirect(
            url_for(
                "summary.view_summary",
                note_id=note.id
            )
        )

    except Exception as e:

        db.session.rollback()

        logger.exception("SUMMARY GENERATION ERROR")

        flash(
            f"Error generating summary: {str(e)}",
            "danger"
        )

        return redirect(url_for("notes.notes"))


# ==========================================================
# View Summary
# ==========================================================
@summary_bp.route("/summary/<int:note_id>")
@login_required
def view_summary(note_id):

    try:

        note = db.session.get(StudyMaterial, note_id)

        if note is None:
            flash("Study material not found.", "danger")
            return redirect(url_for("notes.notes"))

        # Security Check
        if note.user_id != current_user.id:
            flash("Unauthorized access.", "danger")
            return redirect(url_for("notes.notes"))

        # Summary Exists?
        if not note.summary_generated or not note.summary:
            flash(
                "Summary not generated yet.",
                "warning"
            )
            return redirect(url_for("notes.notes"))

        return render_template(
            "summary.html",
            note=note
        )

    except Exception as e:

        logger.exception("VIEW SUMMARY ERROR")

        flash(
            f"Error opening summary: {str(e)}",
            "danger"
        )

        return redirect(url_for("notes.notes"))