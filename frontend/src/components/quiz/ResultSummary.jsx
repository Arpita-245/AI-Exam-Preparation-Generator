import {
  FaCheckCircle,
  FaTimesCircle,
  FaTrophy,
  FaChartLine,
} from "react-icons/fa";

function ResultSummary({
  score,
  total,
  correct,
  wrong,
}) {
  const percentage = Math.round((score / total) * 100);

  let message = "";
  let badge = "";
  let badgeColor = "";

  if (percentage >= 90) {
    message = "Outstanding! Keep it up 🚀";
    badge = "Expert";
    badgeColor = "bg-green-500";
  } else if (percentage >= 75) {
    message = "Excellent Work 🎉";
    badge = "Advanced";
    badgeColor = "bg-blue-500";
  } else if (percentage >= 60) {
    message = "Good Job 👍";
    badge = "Intermediate";
    badgeColor = "bg-yellow-500";
  } else {
    message = "Keep Practicing 💪";
    badge = "Beginner";
    badgeColor = "bg-red-500";
  }

  return (
    <div className="bg-white rounded-3xl shadow-xl p-8">

      <div className="flex flex-col lg:flex-row justify-between items-center gap-8">

        {/* Left Side */}
        <div className="text-center lg:text-left">

          <h2 className="text-4xl font-bold">
            Quiz Completed 🎉
          </h2>

          <p className="text-gray-500 mt-3">
            Here is your performance summary.
          </p>

          <div
            className={`${badgeColor} inline-block mt-5 px-5 py-2 rounded-full text-white font-semibold`}
          >
            {badge}
          </div>

        </div>

        {/* Score Circle */}
        <div
          className="
          w-40
          h-40
          rounded-full
          border-[10px]
          border-blue-600
          flex
          flex-col
          items-center
          justify-center
          "
        >
          <span className="text-5xl font-bold">
            {percentage}%
          </span>

          <span className="text-gray-500">
            Accuracy
          </span>
        </div>

      </div>

      {/* Statistics */}
      <div className="grid md:grid-cols-4 gap-6 mt-10">

        <div className="bg-blue-100 rounded-2xl p-5">
          <FaTrophy className="text-blue-600 text-3xl mb-3" />
          <h3 className="font-semibold">Score</h3>
          <p className="text-3xl font-bold">
            {score}/{total}
          </p>
        </div>

        <div className="bg-green-100 rounded-2xl p-5">
          <FaCheckCircle className="text-green-600 text-3xl mb-3" />
          <h3 className="font-semibold">Correct</h3>
          <p className="text-3xl font-bold">
            {correct}
          </p>
        </div>

        <div className="bg-red-100 rounded-2xl p-5">
          <FaTimesCircle className="text-red-600 text-3xl mb-3" />
          <h3 className="font-semibold">Wrong</h3>
          <p className="text-3xl font-bold">
            {wrong}
          </p>
        </div>

        <div className="bg-purple-100 rounded-2xl p-5">
          <FaChartLine className="text-purple-600 text-3xl mb-3" />
          <h3 className="font-semibold">Accuracy</h3>
          <p className="text-3xl font-bold">
            {percentage}%
          </p>
        </div>

      </div>

      {/* Progress Bar */}
      <div className="mt-10">

        <div className="flex justify-between mb-2">
          <span className="font-medium">
            Overall Performance
          </span>

          <span>{percentage}%</span>
        </div>

        <div className="w-full h-5 bg-gray-200 rounded-full overflow-hidden">

          <div
            className="h-5 bg-gradient-to-r from-blue-500 to-indigo-600 rounded-full transition-all duration-500"
            style={{
              width: `${percentage}%`,
            }}
          />

        </div>

      </div>

      {/* AI Feedback */}
      <div className="mt-10 bg-blue-50 border border-blue-200 rounded-2xl p-6">

        <h3 className="text-2xl font-bold">
          🤖 AI Feedback
        </h3>

        <p className="mt-4 text-gray-700 leading-7">
          {message}
          {" "}
          Continue practicing consistently to improve your
          understanding and maintain your study streak.
        </p>

      </div>

    </div>
  );
}

export default ResultSummary;