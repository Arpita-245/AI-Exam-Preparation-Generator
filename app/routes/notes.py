<<<<<<< HEAD
from flask import Blueprint
from flask import render_template

from flask_login import login_required
from flask_login import current_user

from app.models import StudyMaterial
=======
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from app.models import StudyMaterial
from app.extensions import db
>>>>>>> master

notes_bp = Blueprint("notes", __name__)


<<<<<<< HEAD
@notes_bp.route("/notes")
@login_required
def notes():

    uploaded_notes = StudyMaterial.query.filter_by(

        user_id=current_user.id

    ).all()

    return render_template(

        "my_notes.html",

        notes=uploaded_notes

    )
=======
# ======================================
# VIEW NOTES + SEARCH
# ======================================
@notes_bp.route("/notes")
@login_required
def my_notes():

    # Get search query from URL
    query = request.args.get("q")

    # ======================================
    # SEARCH FUNCTIONALITY
    # ======================================
    if query:
        uploaded_notes = StudyMaterial.query.filter(
            StudyMaterial.user_id == current_user.id,
            StudyMaterial.original_filename.contains(query)
        ).all()
    else:
        uploaded_notes = StudyMaterial.query.filter_by(
            user_id=current_user.id
        ).all()

    return render_template(
        "my_notes.html",
        notes=uploaded_notes,
        search_query=query
    )


# ======================================
# DELETE NOTE (FIX YOUR ERROR)
# ======================================
@notes_bp.route("/delete-note/<int:id>")
@login_required
def delete_note(id):

    # Get note or 404 error
    note = StudyMaterial.query.get_or_404(id)

    # सुरक्षा (IMPORTANT: user can only delete own note)
    if note.user_id != current_user.id:
        return "Unauthorized Access", 403

    # Delete from database
    db.session.delete(note)
    db.session.commit()

    # Redirect back to notes page
    return redirect(url_for("notes.my_notes"))
>>>>>>> master
