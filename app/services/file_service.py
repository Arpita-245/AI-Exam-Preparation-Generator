import os

from werkzeug.utils import secure_filename
from flask import current_app


def save_uploaded_file(file):

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        current_app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    return filename, filepath