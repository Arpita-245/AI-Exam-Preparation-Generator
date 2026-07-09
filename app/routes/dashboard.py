from flask import Blueprint, render_template
from flask_login import login_required, current_user

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    stats = {
        "notes": 0,
        "quizzes": 0,
        "average": 0,
        "subjects": 0
    }

    return render_template(
        "dashboard.html",
        user=current_user,
        stats=stats
    )