function QuestionCard({
  question,
  selectedAnswer,
  setSelectedAnswer,
}) {
  return (
    <div className="bg-white p-8 rounded-xl shadow">

      <h2 className="text-2xl font-bold mb-6">
        {question.question}
      </h2>

      {question.options.map((option, index) => (

        <label
          key={index}
          className="flex items-center gap-3 border rounded-lg p-4 mb-4 cursor-pointer hover:bg-blue-50"
        >

          <input
            type="radio"
            name="option"
            checked={selectedAnswer === option}
            onChange={() => setSelectedAnswer(option)}
          />

          {option}

        </label>

      ))}

    </div>
  );
}

export default QuestionCard;