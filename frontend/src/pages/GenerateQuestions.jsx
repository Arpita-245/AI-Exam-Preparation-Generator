import { useState } from "react";

import DashboardLayout from "../layouts/DashboardLayout";

import QuestionsList from "../components/generate/QuestionsList";

function GenerateQuestions() {
  const [subject, setSubject] = useState("DBMS");
  const [difficulty, setDifficulty] = useState("Medium");
  const [count, setCount] = useState(10);
  const [type, setType] = useState("MCQ");

  const [loading, setLoading] = useState(false);
  const [questions, setQuestions] = useState([]);

  const handleGenerate = () => {
    setLoading(true);

    setTimeout(() => {
      const dummyQuestions = [
        {
          question: "What is a Primary Key?",
          options: [
            "Unique Identifier",
            "Foreign Key",
            "Constraint",
            "Index",
          ],
        },
        {
          question: "Which SQL command retrieves data?",
          options: [
            "INSERT",
            "SELECT",
            "UPDATE",
            "DELETE",
          ],
        },
        {
          question: "Which language is mainly used for React?",
          options: [
            "Python",
            "Java",
            "JavaScript",
            "C++",
          ],
        },
        {
          question: "Which normal form removes partial dependency?",
          options: [
            "1NF",
            "2NF",
            "3NF",
            "BCNF",
          ],
        },
      ];

      setQuestions(dummyQuestions);
      setLoading(false);
    }, 1800);
  };

  return (
    <DashboardLayout>
      {/* Page Heading */}
      <div className="mb-10">
        <h1 className="text-4xl font-bold text-slate-800">
          🧠 AI Question Generator
        </h1>

        <p className="text-gray-500 mt-3">
          Generate intelligent exam questions from your uploaded
          study material.
        </p>
      </div>

      {/* Generator Form */}
      <div className="bg-white rounded-3xl shadow-lg p-8">

        <div className="grid md:grid-cols-2 gap-6">

          {/* Subject */}
          <div>
            <label className="block font-semibold mb-2">
              Subject
            </label>

            <select
              className="w-full border rounded-xl p-3"
              value={subject}
              onChange={(e) => setSubject(e.target.value)}
            >
              <option>DBMS</option>
              <option>Java</option>
              <option>Python</option>
              <option>Artificial Intelligence</option>
              <option>Cloud Computing</option>
            </select>
          </div>

          {/* Difficulty */}
          <div>
            <label className="block font-semibold mb-2">
              Difficulty
            </label>

            <select
              className="w-full border rounded-xl p-3"
              value={difficulty}
              onChange={(e) => setDifficulty(e.target.value)}
            >
              <option>Easy</option>
              <option>Medium</option>
              <option>Hard</option>
            </select>
          </div>

          {/* Number of Questions */}
          <div>
            <label className="block font-semibold mb-2">
              Number of Questions
            </label>

            <input
              type="number"
              min="1"
              max="50"
              className="w-full border rounded-xl p-3"
              value={count}
              onChange={(e) => setCount(e.target.value)}
            />
          </div>

          {/* Question Type */}
          <div>
            <label className="block font-semibold mb-2">
              Question Type
            </label>

            <select
              className="w-full border rounded-xl p-3"
              value={type}
              onChange={(e) => setType(e.target.value)}
            >
              <option>MCQ</option>
              <option>True / False</option>
              <option>Short Answer</option>
              <option>Long Answer</option>
            </select>
          </div>

        </div>

        <button
          onClick={handleGenerate}
          disabled={loading}
          className="
            mt-8
            bg-gradient-to-r
            from-blue-600
            to-indigo-600
            hover:from-blue-700
            hover:to-indigo-700
            text-white
            px-8
            py-3
            rounded-xl
            font-semibold
            transition
            disabled:opacity-70
          "
        >
          {loading
            ? "Generating Questions..."
            : "Generate Questions"}
        </button>
      </div>

      {/* Loading */}
      {loading && (
        <div className="bg-white rounded-3xl shadow-lg p-8 mt-8 text-center">

          <div className="w-12 h-12 border-4 border-blue-600 border-t-transparent rounded-full animate-spin mx-auto"></div>

          <h2 className="mt-5 text-xl font-semibold">
            AI is generating questions...
          </h2>

          <p className="text-gray-500 mt-2">
            Please wait a few seconds.
          </p>

        </div>
      )}

      {/* Questions */}
      {!loading && (
        <QuestionsList questions={questions} />
      )}
    </DashboardLayout>
  );
}

export default GenerateQuestions;