import os

from flask import (
    Flask,
    render_template,
    send_from_directory,
    abort
)

from config import Config
from app.extensions import (
    db,
    migrate,
    login_manager
)


def create_app():

    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )

    # ==================================================
    # Load Configuration
    # ==================================================
    app.config.from_object(Config)

    # ==================================================
    # Secret Key
    # ==================================================
    app.secret_key = app.config["SECRET_KEY"]

    # ==================================================
    # Initialize Extensions
    # ==================================================
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "warning"

    # ==================================================
    # Import Models
    # ==================================================
    from app import models

    # ==================================================
    # Create Database
    # ==================================================
    with app.app_context():
        db.create_all()

    # ==================================================
    # Home Page
    # ==================================================
    @app.route("/")
    def home():
        return render_template("home.html")

    # ==================================================
    # Serve Uploaded Files
    # ==================================================
    @app.route("/uploads/<path:filename>")
    def uploaded_file(filename):

        upload_folder = app.config["UPLOAD_FOLDER"]

        file_path = os.path.join(
            upload_folder,
            filename
        )

        if not os.path.exists(file_path):
            abort(404)

        return send_from_directory(
            directory=upload_folder,
            path=filename,
            as_attachment=False
        )

    # ==================================================
    # Import Blueprints
    # ==================================================
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
    from app.routes.chatbot import chatbot_bp

    # ==================================================
    # Register Blueprints
    # ==================================================
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

    app.register_blueprint(
        chatbot_bp,
        url_prefix="/chatbot"
    )

    # ==================================================
    # Test Route
    # ==================================================
    @app.route("/test-chat")
    def test_chat():
        return "✅ Chatbot route is working!"

    return app