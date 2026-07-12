from flask import Blueprint
from flask import render_template

from flask_login import login_required
from flask_login import current_user

from app.models import QuizResult

result_bp = Blueprint("result", __name__)


@result_bp.route("/results")
@login_required
def results():

    results = (
        QuizResult.query
        .filter_by(user_id=current_user.id)
        .order_by(QuizResult.attempted_on.desc())
        .all()
    )

    return render_template(
        "results.html",
        results=results
    )