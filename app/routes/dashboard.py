import matplotlib
matplotlib.use('Agg')

from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models import StudyMaterial, QuizResult
from sqlalchemy import func

import matplotlib.pyplot as plt
import os
from datetime import datetime

dashboard_bp = Blueprint("dashboard", __name__)


# ======================================
# 📊 DASHBOARD ROUTE
# ======================================
@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    # ======================================
    # Notes Statistics
    # ======================================
    total_notes = StudyMaterial.query.filter_by(
        user_id=current_user.id
    ).count()

    # ======================================
    # Quiz Statistics
    # ======================================
    total_quizzes = QuizResult.query.filter_by(
        user_id=current_user.id
    ).count()

    average_score = (
        QuizResult.query.with_entities(
            func.avg(QuizResult.percentage)
        )
        .filter_by(user_id=current_user.id)
        .scalar()
    )

    average_score = round(average_score, 2) if average_score else 0

    # ======================================
    # Highest & Lowest Score
    # ======================================
    highest_score = (
        QuizResult.query.with_entities(
            func.max(QuizResult.percentage)
        )
        .filter_by(user_id=current_user.id)
        .scalar()
    ) or 0

    lowest_score = (
        QuizResult.query.with_entities(
            func.min(QuizResult.percentage)
        )
        .filter_by(user_id=current_user.id)
        .scalar()
    ) or 0

    # ======================================
    # Quiz History (for charts)
    # ======================================
    quiz_results = (
        QuizResult.query
        .filter_by(user_id=current_user.id)
        .order_by(QuizResult.attempted_on.asc())
        .all()
    )

    quiz_labels = []
    quiz_scores = []

    for i, result in enumerate(quiz_results, start=1):
        quiz_labels.append(f"Quiz {i}")
        quiz_scores.append(result.percentage)

    # ======================================
    # 📊 Generate Chart
    # ======================================
    chart_filename = generate_progress_chart(quiz_scores)

    # ======================================
    # Dashboard Data
    # ======================================
    stats = {
        "notes": total_notes,
        "quizzes": total_quizzes,
        "average": average_score,
        "subjects": total_notes,
        "highest": highest_score,
        "lowest": lowest_score
    }

    return render_template(
        "dashboard.html",
        user=current_user,
        stats=stats,
        quiz_labels=quiz_labels,
        quiz_scores=quiz_scores,
        chart_file=chart_filename  # 🔥 send chart to frontend
    )


# ======================================
# 📈 MATPLOTLIB GRAPH FUNCTION
# ======================================
def generate_progress_chart(scores):

    if not scores:
        scores = [0]

    attempts = list(range(1, len(scores) + 1))

    # 🔥 Modern styling
    plt.figure(figsize=(8, 4))
    plt.plot(attempts, scores, marker='o', linewidth=2)

    plt.xlabel("Attempt")
    plt.ylabel("Score (%)")
    plt.title("Performance Over Time")
    plt.grid(True)

    # Ensure static folder exists
    static_path = os.path.join("app", "static", "charts")
    os.makedirs(static_path, exist_ok=True)

    # 🔥 Unique filename (VERY IMPORTANT)
    filename = f"chart_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    file_path = os.path.join(static_path, filename)

    plt.savefig(file_path, bbox_inches='tight')
    plt.close()

    return f"charts/{filename}"  # 🔥 return relative path


# ======================================
# 🔁 OPTIONAL ROUTE (Manual Graph Trigger)
# ======================================
@dashboard_bp.route("/progress-chart")
@login_required
def progress_chart():

    results = QuizResult.query.filter_by(user_id=current_user.id).all()

    scores = [r.percentage for r in results]

    chart_file = generate_progress_chart(scores)

    return f"Chart Generated Successfully: {chart_file}"