import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:

    # Secret Key
    SECRET_KEY = "exam_project_secret_key"

    # Database
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        BASE_DIR,
        "instance",
        "database.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload Configuration
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

    MAX_CONTENT_LENGTH = 20 * 1024 * 1024      # 20 MB

    ALLOWED_EXTENSIONS = {"pdf", "docx", "txt"}