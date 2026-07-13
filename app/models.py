from app.extensions import db
from flask_login import UserMixin


# ==================================================
# User Model
# ==================================================

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

    # Relationships
    study_materials = db.relationship(
        "StudyMaterial",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    quiz_results = db.relationship(
        "QuizResult",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User {self.email}>"


# ==================================================
# Study Material Model
# ==================================================

class StudyMaterial(db.Model):
    __tablename__ = "study_materials"

    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(
        db.String(255),
        nullable=False
    )

    file_path = db.Column(
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

    # ===============================
    # Extracted Text
    # ===============================

    extracted_text = db.Column(db.Text)

    # ===============================
    # AI Summary
    # ===============================

    summary = db.Column(db.Text)

    summary_generated = db.Column(
        db.Boolean,
        default=False
    )

    # ===============================
    # AI Quiz
    # ===============================

    quiz = db.Column(db.Text)

    quiz_generated = db.Column(
        db.Boolean,
        default=False
    )

    # ===============================
    # AI Recommendation
    # ===============================

    recommendation = db.Column(db.Text)

    recommendation_generated = db.Column(
        db.Boolean,
        default=False
    )

    # ===============================
    # Foreign Key
    # ===============================

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    # ===============================
    # Relationships
    # ===============================

    user = db.relationship(
        "User",
        back_populates="study_materials"
    )

    quiz_results = db.relationship(
        "QuizResult",
        back_populates="study_material",
        cascade="all, delete-orphan"
    )

    # ===============================
    # Utility Properties
    # ===============================

    @property
    def has_summary(self):
        return bool(self.summary_generated and self.summary)

    @property
    def has_quiz(self):
        return bool(self.quiz_generated and self.quiz)

    @property
    def has_recommendation(self):
        return bool(
            self.recommendation_generated and
            self.recommendation
        )

    def __repr__(self):
        return f"<StudyMaterial {self.original_filename}>"


# ==================================================
# Quiz Result Model
# ==================================================

class QuizResult(db.Model):
    __tablename__ = "quiz_results"

    id = db.Column(db.Integer, primary_key=True)

    score = db.Column(
        db.Integer,
        nullable=False
    )

    total_questions = db.Column(
        db.Integer,
        nullable=False
    )

    percentage = db.Column(
        db.Float,
        nullable=False
    )

    attempted_on = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    # ===============================
    # Foreign Keys
    # ===============================

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

    # ===============================
    # Relationships
    # ===============================

    study_material = db.relationship(
        "StudyMaterial",
        back_populates="quiz_results"
    )

    user = db.relationship(
        "User",
        back_populates="quiz_results"
    )

    # ===============================
    # Utility Properties
    # ===============================

    @property
    def is_pass(self):
        return self.percentage >= 50

    def __repr__(self):
        return (
            f"<QuizResult "
            f"{self.score}/{self.total_questions}>"
        )