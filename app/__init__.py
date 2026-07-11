from flask import Flask, render_template
from config import Config
from app.extensions import db, login_manager, migrate

# ✅ ADD THIS IMPORT
from app.routes.chatbot import chatbot_bp


def create_app():

    app = Flask(__name__)

    # ==========================================
    # Load Configuration
    # ==========================================
    app.config.from_object(Config)

    # ==========================================
    # Initialize Extensions
    # ==========================================
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # ==========================================
    # Import Models
    # ==========================================
    from app import models

    # ==========================================
    # 🔥 LANDING PAGE ROUTE
    # ==========================================
    @app.route("/")
    def home():
        return render_template("home.html")

    # ==========================================
    # Import Blueprints
    # ==========================================
    from app.routes.auth import auth_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.upload import upload_bp
    from app.routes.notes import notes_bp
    from app.routes.summary import summary_bp
    from app.routes.quiz import quiz_bp
    from app.routes.exam import exam_bp
    from app.routes.result import result_bp
    from app.routes.recommendation import recommendation_bp
    from app.routes.pdf import pdf_bp

    # ==========================================
    # Register Blueprints
    # ==========================================
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(upload_bp)
    app.register_blueprint(notes_bp)
    app.register_blueprint(summary_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(exam_bp)
    app.register_blueprint(result_bp)
    app.register_blueprint(recommendation_bp)
    app.register_blueprint(pdf_bp)

    # ✅ ADD THIS LINE (VERY IMPORTANT)
    app.register_blueprint(chatbot_bp)

    return app