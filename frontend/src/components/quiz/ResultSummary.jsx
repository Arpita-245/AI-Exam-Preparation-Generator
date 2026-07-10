function ResultSummary({
  score,
  total,
  correct,
  wrong,
}) {

  const percentage = Math.round((score / total) * 100);

  let message = "";

  if (percentage >= 80) {
    message = "Excellent Work 🎉";
  } else if (percentage >= 60) {
    message = "Good Job 👍";
  } else {
    message = "Keep Practicing 💪";
  }

  return (
    <div className="bg-white rounded-xl shadow-lg p-8">

      <h2 className="text-3xl font-bold text-center mb-8">
        Quiz Completed
      </h2>

      <div className="grid grid-cols-2 gap-6">

        <div className="bg-blue-100 rounded-lg p-5">

          <h3>Score</h3>

          <p className="text-4xl font-bold">
            {score}/{total}
          </p>

        </div>

        <div className="bg-green-100 rounded-lg p-5">

          <h3>Accuracy</h3>

          <p className="text-4xl font-bold">
            {percentage}%
          </p>

        </div>

        <div className="bg-emerald-100 rounded-lg p-5">

          <h3>Correct</h3>

          <p className="text-4xl font-bold">
            {correct}
          </p>

        </div>

        <div className="bg-red-100 rounded-lg p-5">

          <h3>Wrong</h3>

          <p className="text-4xl font-bold">
            {wrong}
          </p>

        </div>

      </div>

      <div className="mt-10">

        <div className="w-full h-5 bg-gray-200 rounded-full">

          <div
            className="h-5 bg-blue-600 rounded-full"
            style={{
              width: `${percentage}%`,
            }}
          />

        </div>

      </div>

      <h3 className="text-center text-2xl font-bold mt-8">
        {message}
      </h3>

    </div>
  );
}

export default ResultSummary;