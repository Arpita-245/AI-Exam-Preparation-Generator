from flask import Blueprint
from flask import render_template

from flask_login import login_required
from flask_login import current_user

from app.models import StudyMaterial

notes_bp = Blueprint("notes", __name__)


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