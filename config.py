import os
from dotenv import load_dotenv

# ===================================
# Load environment variables
# ===================================
load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:

<<<<<<< HEAD
    # Secret Key
    SECRET_KEY = "exam_project_secret_key"

    # Database
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        BASE_DIR,
        "instance",
        "database.db"
=======
    # ===================================
    # 🔐 Flask Configuration
    # ===================================
    SECRET_KEY = os.getenv("SECRET_KEY", "exam_project_secret_key")

    # ===================================
    # 🗄️ Database Configuration
    # ===================================
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "instance", "database.db")
>>>>>>> master
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

<<<<<<< HEAD
    # Upload Configuration
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

    MAX_CONTENT_LENGTH = 20 * 1024 * 1024      # 20 MB

    ALLOWED_EXTENSIONS = {"pdf", "docx", "txt"}
=======
    # ===================================
    # 📂 Upload Folder
    # ===================================
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

    # Create folder if not exists
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # Maximum Upload Size (16 MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # ===================================
    # 🤖 Groq AI Configuration
    # ===================================
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

    # ===================================
    # 📄 PDF Processing (NEW)
    # ===================================
    PDF_MAX_CHARS = 3000   # limit for AI input

    # ===================================
    # ⚙️ Session Configuration
    # ===================================
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
>>>>>>> master
