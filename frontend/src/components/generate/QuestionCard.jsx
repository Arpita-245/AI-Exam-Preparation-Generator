function QuestionCard({ question, index }) {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">
      <h3 className="text-xl font-semibold mb-5">
        {index + 1}. {question.question}
      </h3>

      <div className="space-y-3">
        {question.options.map((option, i) => (
          <label
            key={i}
            className="flex items-center gap-3 border rounded-xl p-3 hover:bg-blue-50 cursor-pointer"
          >
            <input
              type="radio"
              name={`question-${index}`}
            />

            <span>
              {String.fromCharCode(65 + i)}.
            </span>

            <span>{option}</span>
          </label>
        ))}
      </div>
    </div>
  );
}

export default QuestionCard;