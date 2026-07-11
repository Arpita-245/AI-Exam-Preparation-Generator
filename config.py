import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:

    # ===================================
    # Flask Configuration
    # ===================================

    SECRET_KEY = "exam_project_secret_key"

    # ===================================
    # Database Configuration
    # ===================================

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        BASE_DIR,
        "instance",
        "database.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ===================================
    # Upload Folder
    # ===================================

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

    # Maximum Upload Size (16 MB)

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # ===================================
    # Groq AI Configuration
    # ===================================

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    GROQ_MODEL = os.getenv("GROQ_MODEL")