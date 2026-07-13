import os
from datetime import datetime

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user

from sqlalchemy import func

from app.models import StudyMaterial, QuizResult

dashboard_bp = Blueprint("dashboard", __name__)


# ==================================================
# Dashboard
# ==================================================
@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    try:

        # ------------------------------------------
        # Notes Statistics
        # ------------------------------------------
        total_notes = StudyMaterial.query.filter_by(
            user_id=current_user.id
        ).count()

        # ------------------------------------------
        # Quiz Statistics
        # ------------------------------------------
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

        highest_score = (
            QuizResult.query.with_entities(
                func.max(QuizResult.percentage)
            )
            .filter_by(user_id=current_user.id)
            .scalar()
        )

        highest_score = round(highest_score, 2) if highest_score else 0

        lowest_score = (
            QuizResult.query.with_entities(
                func.min(QuizResult.percentage)
            )
            .filter_by(user_id=current_user.id)
            .scalar()
        )

        lowest_score = round(lowest_score, 2) if lowest_score else 0

        # ------------------------------------------
        # Quiz History
        # ------------------------------------------
        quiz_results = (
            QuizResult.query
            .filter_by(user_id=current_user.id)
            .order_by(QuizResult.attempted_on.asc())
            .all()
        )

        quiz_labels = []
        quiz_scores = []

        for index, result in enumerate(quiz_results, start=1):
            quiz_labels.append(f"Quiz {index}")
            quiz_scores.append(result.percentage)

        # ------------------------------------------
        # Generate Performance Chart
        # ------------------------------------------
        chart_filename = generate_progress_chart(quiz_scores)

        stats = {
            "notes": total_notes,
            "quizzes": total_quizzes,
            "average": average_score,
            "highest": highest_score,
            "lowest": lowest_score,
            "subjects": total_notes
        }

        return render_template(
            "dashboard.html",
            user=current_user,
            stats=stats,
            quiz_labels=quiz_labels,
            quiz_scores=quiz_scores,
            chart_file=chart_filename
        )

    except Exception as e:
        print("DASHBOARD ERROR:", e)

        flash(f"Dashboard Error: {str(e)}", "danger")

        return render_template(
            "dashboard.html",
            user=current_user,
            stats={
                "notes": 0,
                "quizzes": 0,
                "average": 0,
                "highest": 0,
                "lowest": 0,
                "subjects": 0
            },
            quiz_labels=[],
            quiz_scores=[],
            chart_file=""
        )


# ==================================================
# Generate Progress Chart
# ==================================================
def generate_progress_chart(scores):

    if not scores:
        scores = [0]

    attempts = list(range(1, len(scores) + 1))

    plt.figure(figsize=(8, 4))
    plt.plot(attempts, scores, marker="o", linewidth=2)

    plt.xlabel("Attempt")
    plt.ylabel("Score (%)")
    plt.title("Performance Over Time")
    plt.grid(True)

    chart_folder = os.path.join("app", "static", "charts")
    os.makedirs(chart_folder, exist_ok=True)

    filename = f"chart_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"

    filepath = os.path.join(chart_folder, filename)

    plt.savefig(filepath, bbox_inches="tight")
    plt.close()

    return f"charts/{filename}"


# ==================================================
# Manual Chart Route
# ==================================================
@dashboard_bp.route("/progress-chart")
@login_required
def progress_chart():

    results = QuizResult.query.filter_by(
        user_id=current_user.id
    ).all()

    scores = [r.percentage for r in results]

    chart = generate_progress_chart(scores)

    return f"Chart generated successfully: {chart}"