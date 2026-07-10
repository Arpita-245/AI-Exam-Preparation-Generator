function QuizNavigation({
  currentQuestion,
  totalQuestions,
  nextQuestion,
  previousQuestion,
}) {
  return (
    <div className="flex justify-between mt-8">

      <button
        onClick={previousQuestion}
        disabled={currentQuestion === 0}
        className="bg-gray-500 text-white px-6 py-3 rounded"
      >
        Previous
      </button>

      <button
        onClick={nextQuestion}
        className="bg-blue-600 text-white px-6 py-3 rounded"
      >
        {currentQuestion === totalQuestions - 1
          ? "Finish Quiz"
          : "Next"}
      </button>

    </div>
  );
}

export default QuizNavigation;