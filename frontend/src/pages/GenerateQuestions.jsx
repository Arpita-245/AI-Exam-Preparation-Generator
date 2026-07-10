import { useState } from "react";
import DashboardLayout from "../layouts/DashboardLayout";

function GenerateQuestions() {
  const [subject, setSubject] = useState("DBMS");
  const [difficulty, setDifficulty] = useState("Medium");
  const [count, setCount] = useState(10);
  const [type, setType] = useState("MCQ");
  const [questions, setQuestions] = useState([]);

  const handleGenerate = () => {
    const dummyQuestions = [
      {
        question: "What is a Primary Key?",
        options: [
          "Unique identifier",
          "Foreign Key",
          "Index",
          "Constraint"
        ]
      },
      {
        question: "Which SQL command retrieves data?",
        options: [
          "INSERT",
          "SELECT",
          "UPDATE",
          "DELETE"
        ]
      }
    ];

    setQuestions(dummyQuestions);
  };

  return (
    <DashboardLayout>

      <h1 className="text-4xl font-bold mb-8">
        Generate AI Questions
      </h1>

      <div className="bg-white rounded-xl shadow p-8">

        <div className="grid md:grid-cols-2 gap-6">

          <div>

            <label className="block mb-2 font-medium">
              Subject
            </label>

            <select
              className="w-full border p-3 rounded"
              value={subject}
              onChange={(e) => setSubject(e.target.value)}
            >
              <option>DBMS</option>
              <option>Python</option>
              <option>Java</option>
              <option>AI</option>
            </select>

          </div>

          <div>

            <label className="block mb-2 font-medium">
              Difficulty
            </label>

            <select
              className="w-full border p-3 rounded"
              value={difficulty}
              onChange={(e) => setDifficulty(e.target.value)}
            >
              <option>Easy</option>
              <option>Medium</option>
              <option>Hard</option>
            </select>

          </div>

          <div>

            <label className="block mb-2 font-medium">
              Number of Questions
            </label>

            <input
              type="number"
              className="w-full border p-3 rounded"
              value={count}
              onChange={(e) => setCount(e.target.value)}
            />

          </div>

          <div>

            <label className="block mb-2 font-medium">
              Question Type
            </label>

            <select
              className="w-full border p-3 rounded"
              value={type}
              onChange={(e) => setType(e.target.value)}
            >
              <option>MCQ</option>
              <option>True / False</option>
              <option>Short Answer</option>
            </select>

          </div>

        </div>

        <button
          onClick={handleGenerate}
          className="mt-8 bg-blue-600 text-white px-8 py-3 rounded-lg"
        >
          Generate Questions
        </button>

      </div>

      {questions.length > 0 && (

        <div className="mt-10 bg-white p-8 rounded-xl shadow">

          <h2 className="text-2xl font-bold mb-6">
            Generated Questions
          </h2>

          {questions.map((q, index) => (

            <div
              key={index}
              className="mb-8"
            >

              <h3 className="font-semibold mb-4">

                {index + 1}. {q.question}

              </h3>

              {q.options.map((option, i) => (

                <p key={i} className="ml-4 mb-2">

                  {String.fromCharCode(65 + i)}. {option}

                </p>

              ))}

            </div>

          ))}

        </div>

      )}

    </DashboardLayout>
  );
}

export default GenerateQuestions;