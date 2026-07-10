import { useState } from "react";
import DashboardLayout from "../layouts/DashboardLayout";
import QuizTimer from "../components/quiz/QuizTimer";
import QuestionCard from "../components/quiz/QuestionCard";
import QuizNavigation from "../components/quiz/QuizNavigation";

function Quiz() {

  const questions = [
    {
      question: "Which SQL command retrieves data?",
      options: [
        "INSERT",
        "UPDATE",
        "SELECT",
        "DELETE",
      ],
    },
    {
      question: "Which language is used in React?",
      options: [
        "Python",
        "Java",
        "JavaScript",
        "PHP",
      ],
    },
  ];

  const [currentQuestion, setCurrentQuestion] = useState(0);

  const [selectedAnswer, setSelectedAnswer] = useState("");

  const nextQuestion = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
      setSelectedAnswer("");
    }
  };

  const previousQuestion = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(currentQuestion - 1);
      setSelectedAnswer("");
    }
  };

  return (
    <DashboardLayout>

      <div className="flex justify-between items-center mb-8">

        <h1 className="text-4xl font-bold">
          Quiz
        </h1>

        <QuizTimer />

      </div>

      <QuestionCard
        question={questions[currentQuestion]}
        selectedAnswer={selectedAnswer}
        setSelectedAnswer={setSelectedAnswer}
      />

      <QuizNavigation
        currentQuestion={currentQuestion}
        totalQuestions={questions.length}
        nextQuestion={nextQuestion}
        previousQuestion={previousQuestion}
      />

    </DashboardLayout>
  );
}

export default Quiz;