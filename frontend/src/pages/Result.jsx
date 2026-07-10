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

      <div className="flex justify-center gap-6 mt-10">

        <Link
          to="/quiz"
          className="bg-blue-600 text-white px-6 py-3 rounded-lg"
        >
          Retry Quiz
        </Link>

        <Link
          to="/dashboard"
          className="bg-green-600 text-white px-6 py-3 rounded-lg"
        >
          Dashboard
        </Link>

      </div>

    </DashboardLayout>
  );
}

export default Result;