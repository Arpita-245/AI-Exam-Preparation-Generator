from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    url_for
)

from flask_login import (
    login_required,
    current_user
)

from app.extensions import db
from app.models import QuizResult

import logging

# ==================================================
# Blueprint
# ==================================================
result_bp = Blueprint(
    "result",
    __name__
)

# ==================================================
# Logger
# ==================================================
logger = logging.getLogger(__name__)


# ==================================================
# View Quiz Results
# ==================================================
@result_bp.route("/results", methods=["GET"])
@login_required
def results():

    try:

        quiz_results = (
            QuizResult.query
            .filter_by(user_id=current_user.id)
            .order_by(
                QuizResult.attempted_on.desc()
            )
            .all()
        )

        if len(quiz_results) == 0:
            flash(
                "No quiz results found.",
                "info"
            )

        return render_template(
            "results.html",
            results=quiz_results
        )

    except Exception as e:

        db.session.rollback()

        logger.error(
            f"RESULT ERROR: {str(e)}"
        )

        flash(
            "Unable to load quiz results.",
            "danger"
        )

        return redirect(
            url_for("dashboard.dashboard")
        )


# ==================================================
# Delete Quiz Result (Optional)
# ==================================================
@result_bp.route("/delete-result/<int:id>")
@login_required
def delete_result(id):

    try:

        result = QuizResult.query.get_or_404(id)

        if result.user_id != current_user.id:

            flash(
                "Unauthorized access.",
                "danger"
            )

            return redirect(
                url_for("result.results")
            )

        db.session.delete(result)
        db.session.commit()

        flash(
            "Result deleted successfully.",
            "success"
        )

    except Exception as e:

        db.session.rollback()

        logger.error(
            f"DELETE RESULT ERROR: {str(e)}"
        )

        flash(
            "Unable to delete result.",
            "danger"
        )

    return redirect(
        url_for("result.results")
    )