import os
import logging

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    current_app
)

from flask_login import (
    login_required,
    current_user
)

from app.extensions import db
from app.models import StudyMaterial


notes_bp = Blueprint("notes", __name__)

logger = logging.getLogger(__name__)


# ==========================================================
# My Notes
# ==========================================================
@notes_bp.route("/notes")
@login_required
def notes():

    try:

        search_query = request.args.get("q", "").strip()

        query = StudyMaterial.query.filter_by(
            user_id=current_user.id
        )

        if search_query:
            query = query.filter(
                StudyMaterial.original_filename.ilike(
                    f"%{search_query}%"
                )
            )

        uploaded_notes = (
            query.order_by(
                StudyMaterial.upload_date.desc(),
                StudyMaterial.id.desc()
            )
            .all()
        )

        return render_template(
            "my_notes.html",
            notes=uploaded_notes,
            search_query=search_query
        )

    except Exception as e:

        logger.exception(e)

        flash(
            "Unable to load notes.",
            "danger"
        )

        return render_template(
            "my_notes.html",
            notes=[],
            search_query=""
        )


# ==========================================================
# View Note
# ==========================================================
@notes_bp.route("/note/<int:id>")
@login_required
def view_note(id):

    note = StudyMaterial.query.get_or_404(id)

    if note.user_id != current_user.id:

        flash(
            "Unauthorized access.",
            "danger"
        )

        return redirect(
            url_for("notes.notes")
        )

    return render_template(
        "view_note.html",
        note=note
    )


# ==========================================================
# Delete Note
# ==========================================================
@notes_bp.route("/delete-note/<int:id>", methods=["POST"])
@login_required
def delete_note(id):

    note = StudyMaterial.query.get_or_404(id)

    if note.user_id != current_user.id:

        flash(
            "Unauthorized access.",
            "danger"
        )

        return redirect(
            url_for("notes.notes")
        )

    try:

        # Delete uploaded file
        file_path = os.path.join(
            current_app.config["UPLOAD_FOLDER"],
            note.filename
        )

        if os.path.exists(file_path):
            os.remove(file_path)

        db.session.delete(note)
        db.session.commit()

        flash(
            "Study material deleted successfully.",
            "success"
        )

    except Exception as e:

        db.session.rollback()

        logger.exception(e)

        flash(
            "Unable to delete study material.",
            "danger"
        )

    return redirect(
        url_for("notes.notes")
    )