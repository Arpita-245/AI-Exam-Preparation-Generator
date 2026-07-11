import QuestionCard from "./QuestionCard";

function QuestionsList({ questions }) {
  if (!questions.length) return null;

  return (
    <div className="mt-10">
      <h2 className="text-3xl font-bold mb-6">
        Generated Questions
      </h2>

      <div className="space-y-6">
        {questions.map((question, index) => (
          <QuestionCard
            key={index}
            question={question}
            index={index}
          />
        ))}
      </div>
    </div>
  );
}

export default QuestionsList;