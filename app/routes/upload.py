import os

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    flash,
    current_app,
    url_for
)

from flask_login import login_required, current_user

from app.extensions import db
from app.models import StudyMaterial

from app.utils.file_validator import allowed_file
from app.services.file_service import save_uploaded_file
from app.services.ai_service import process_document

upload_bp = Blueprint("upload", __name__)


@upload_bp.route("/upload", methods=["GET", "POST"])
@login_required
def upload():

    if request.method == "POST":

        if "file" not in request.files:
            flash("No file selected")
            return redirect(request.url)

        file = request.files["file"]

        if file.filename == "":
            flash("Please choose a file")
            return redirect(request.url)

        if allowed_file(file.filename):

            filename, filepath = save_uploaded_file(file)

            # Extract text from uploaded document
            text = process_document(filepath)

            study_material = StudyMaterial(
                filename=filename,
                original_filename=file.filename,
                file_type=file.filename.rsplit(".", 1)[1].lower(),
                file_size=os.path.getsize(filepath),
                extracted_text=text,
                user_id=current_user.id
            )

            db.session.add(study_material)
            db.session.commit()

            flash("File uploaded successfully!")

            return redirect(url_for("upload.upload"))

        flash("Only PDF, DOCX and TXT files are allowed.")

    return render_template("upload.html")