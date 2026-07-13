import os

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    flash,
    url_for,
    current_app
)

from flask_login import (
    login_required,
    current_user
)

from app.extensions import db
from app.models import StudyMaterial

from app.utils.file_validator import allowed_file
from app.services.file_service import save_uploaded_file
from app.services.ai_service import process_document


upload_bp = Blueprint("upload", __name__)


# ==================================================
# Upload Study Material
# ==================================================
@upload_bp.route("/upload", methods=["GET", "POST"])
@login_required
def upload():

    if request.method == "POST":

        # -------------------------------
        # Check if file exists
        # -------------------------------
        if "file" not in request.files:
            flash("No file selected.", "danger")
            return redirect(request.url)

        file = request.files["file"]

        if file.filename.strip() == "":
            flash("Please choose a file.", "warning")
            return redirect(request.url)

        # -------------------------------
        # Validate extension
        # -------------------------------
        if not allowed_file(file.filename):
            flash("Only PDF, DOCX and TXT files are allowed.", "danger")
            return redirect(request.url)

        try:

            # -------------------------------
            # Save uploaded file
            # -------------------------------
            filename, file_path = save_uploaded_file(file)

            full_path = os.path.join(
                current_app.config["UPLOAD_FOLDER"],
                filename
            )

            print("\n" + "=" * 60)
            print("FILE UPLOADED SUCCESSFULLY")
            print("Filename :", filename)
            print("Full Path:", full_path)
            print("=" * 60 + "\n")

            # -------------------------------
            # Extract document text
            # -------------------------------
            extracted_text = process_document(full_path)

            if extracted_text is None:
                extracted_text = ""

            # -------------------------------
            # Save to database
            # -------------------------------
            note = StudyMaterial(
                filename=filename,
                file_path=file_path,
                original_filename=file.filename,
                file_type=file.filename.rsplit(".", 1)[1].lower(),
                file_size=os.path.getsize(full_path),
                extracted_text=extracted_text,
                summary="",
                summary_generated=False,
                quiz="",
                quiz_generated=False,
                recommendation="",
                recommendation_generated=False,
                user_id=current_user.id
            )

            db.session.add(note)
            db.session.commit()

            flash(
                "Study material uploaded successfully!",
                "success"
            )

            return redirect(
                url_for("notes.notes")
            )

        except Exception as e:

            db.session.rollback()

            print("\n========== UPLOAD ERROR ==========")
            print(e)
            print("==================================\n")

            flash(
                f"Upload failed: {str(e)}",
                "danger"
            )

            return redirect(request.url)

    return render_template("upload.html")