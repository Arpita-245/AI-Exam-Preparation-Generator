import os
from dotenv import load_dotenv

# =====================================================
# Load Environment Variables
# =====================================================
load_dotenv()

# =====================================================
# Project Base Directory
# =====================================================
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# =====================================================
# Instance Folder
# =====================================================
INSTANCE_FOLDER = os.path.join(BASE_DIR, "instance")

# =====================================================
# Upload Folder
# =====================================================
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

# Create folders if they don't exist
os.makedirs(INSTANCE_FOLDER, exist_ok=True)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


class Config:

    # =====================================================
    # Flask
    # =====================================================
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "exam_project_secret_key"
    )

    DEBUG = True

    # =====================================================
    # Database
    # =====================================================
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{os.path.join(INSTANCE_FOLDER, 'database.db')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # =====================================================
    # Upload Settings
    # =====================================================
    UPLOAD_FOLDER = UPLOAD_FOLDER

    MAX_CONTENT_LENGTH = 20 * 1024 * 1024

    ALLOWED_EXTENSIONS = {
        "pdf",
        "docx",
        "txt"
    }

    # =====================================================
    # AI Configuration
    # =====================================================
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    GROQ_MODEL = os.getenv(
        "GROQ_MODEL",
        "llama-3.1-8b-instant"
    )

    AI_TEMPERATURE = 0.4
    AI_MAX_TOKENS = 2048
    PDF_MAX_CHARS = 6000

    # =====================================================
    # Session
    # =====================================================
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"

    # =====================================================
    # File Preview
    # =====================================================
    SEND_FILE_MAX_AGE_DEFAULT = 0