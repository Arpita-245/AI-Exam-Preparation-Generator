from app.extensions import db
from flask_login import UserMixin


<<<<<<< HEAD
# ---------------- User Model ---------------- #
=======
# ==================================================
# User Model
# ==================================================
>>>>>>> master

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(100), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    role = db.Column(db.String(20), default="student")

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def __repr__(self):
        return f"<User {self.email}>"


<<<<<<< HEAD
# ---------------- Study Material Model ---------------- #
=======
# ==================================================
# Study Material Model
# ==================================================
>>>>>>> master

class StudyMaterial(db.Model):
    __tablename__ = "study_materials"

    id = db.Column(db.Integer, primary_key=True)

<<<<<<< HEAD
    filename = db.Column(db.String(255), nullable=False)

    original_filename = db.Column(db.String(255), nullable=False)

    file_type = db.Column(db.String(20), nullable=False)

    file_size = db.Column(db.Integer)

    upload_date = db.Column(db.DateTime, server_default=db.func.now())

    # NEW COLUMN
    extracted_text = db.Column(db.Text)

=======
    filename = db.Column(
        db.String(255),
        nullable=False
    )

    original_filename = db.Column(
        db.String(255),
        nullable=False
    )

    file_type = db.Column(
        db.String(20),
        nullable=False
    )

    file_size = db.Column(db.Integer)

    upload_date = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    # ==========================================
    # Extracted Text
    # ==========================================

    extracted_text = db.Column(db.Text)

    # ==========================================
    # AI Summary
    # ==========================================

    summary = db.Column(db.Text)

    summary_generated = db.Column(
        db.Boolean,
        default=False
    )

    # ==========================================
    # AI Quiz
    # ==========================================

    quiz = db.Column(db.Text)

    quiz_generated = db.Column(
        db.Boolean,
        default=False
    )

    # ==========================================
    # AI Recommendation (NEW)
    # ==========================================

    recommendation = db.Column(db.Text)

    recommendation_generated = db.Column(
        db.Boolean,
        default=False
    )

    # ==========================================
    # Relationship
    # ==========================================

>>>>>>> master
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    def __repr__(self):
<<<<<<< HEAD
        return f"<StudyMaterial {self.original_filename}>"
=======
        return f"<StudyMaterial {self.original_filename}>"

# ==================================================
# Quiz Result Model (NEW)
# ==================================================

class QuizResult(db.Model):

    __tablename__ = "quiz_results"

    id = db.Column(db.Integer, primary_key=True)

    score = db.Column(db.Integer, nullable=False)

    total_questions = db.Column(db.Integer, nullable=False)

    percentage = db.Column(db.Float, nullable=False)

    attempted_on = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    study_material_id = db.Column(
        db.Integer,
        db.ForeignKey("study_materials.id"),
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    study_material = db.relationship(
        "StudyMaterial",
        backref="quiz_results"
    )

    def __repr__(self):
        return f"<QuizResult Score={self.score}>"
>>>>>>> master
