import DashboardLayout from "../layouts/DashboardLayout";
import ResultSummary from "../components/quiz/ResultSummary";
import { Link } from "react-router-dom";

function Result() {
  return (
    <DashboardLayout>

      <ResultSummary
        score={8}
        total={10}
        correct={8}
        wrong={2}
      />

      <div className="flex flex-wrap justify-center gap-5 mt-10">

        <Link
          to="/quiz"
          className="
          bg-blue-600
          hover:bg-blue-700
          text-white
          px-8
          py-3
          rounded-xl
          transition
          "
        >
          🔄 Retry Quiz
        </Link>

        <Link
          to="/generate"
          className="
          bg-purple-600
          hover:bg-purple-700
          text-white
          px-8
          py-3
          rounded-xl
          transition
          "
        >
          🧠 Generate New Quiz
        </Link>

        <Link
          to="/dashboard"
          className="
          bg-green-600
          hover:bg-green-700
          text-white
          px-8
          py-3
          rounded-xl
          transition
          "
        >
          🏠 Dashboard
        </Link>

      </div>

    </DashboardLayout>
  );
}

export default Result;