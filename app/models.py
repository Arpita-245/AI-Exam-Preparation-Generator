from app.extensions import db
from flask_login import UserMixin


# ---------------- User Model ---------------- #

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(100), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    role = db.Column(db.String(20), default="student")

    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f"<User {self.email}>"


# ---------------- Study Material Model ---------------- #

class StudyMaterial(db.Model):
    __tablename__ = "study_materials"

    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(db.String(255), nullable=False)

    original_filename = db.Column(db.String(255), nullable=False)

    file_type = db.Column(db.String(20), nullable=False)

    file_size = db.Column(db.Integer)

    upload_date = db.Column(db.DateTime, server_default=db.func.now())

    # NEW COLUMN
    extracted_text = db.Column(db.Text)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    def __repr__(self):
        return f"<StudyMaterial {self.original_filename}>"