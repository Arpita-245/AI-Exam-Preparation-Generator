import { useState } from "react";
import DashboardLayout from "../layouts/DashboardLayout";
import { Link } from "react-router-dom";
import {
  FaSearch,
  FaHistory,
  FaRedo,
  FaEye,
} from "react-icons/fa";

function History() {
  const [search, setSearch] = useState("");

  const history = [
    {
      id: 1,
      subject: "DBMS",
      difficulty: "Medium",
      score: 8,
      total: 10,
      date: "10 July 2026",
    },
    {
      id: 2,
      subject: "Python",
      difficulty: "Easy",
      score: 10,
      total: 10,
      date: "09 July 2026",
    },
    {
      id: 3,
      subject: "Java",
      difficulty: "Hard",
      score: 7,
      total: 10,
      date: "08 July 2026",
    },
  ];

  const filteredHistory = history.filter((quiz) =>
    quiz.subject.toLowerCase().includes(search.toLowerCase())
  );

  const badgeColor = (percentage) => {
    if (percentage >= 80)
      return "bg-green-100 text-green-700";

    if (percentage >= 60)
      return "bg-yellow-100 text-yellow-700";

    return "bg-red-100 text-red-700";
  };

  return (
    <DashboardLayout>

      {/* Heading */}

      <div className="flex flex-col lg:flex-row justify-between items-center mb-10 gap-5">

        <div>

          <h1 className="text-4xl font-bold flex items-center gap-3">

            <FaHistory className="text-blue-600" />

            Quiz History

          </h1>

          <p className="text-gray-500 mt-2">
            Review your previous quiz attempts.
          </p>

        </div>

        {/* Search */}

        <div className="relative w-full lg:w-96">

          <FaSearch
            className="absolute left-4 top-4 text-gray-400"
          />

          <input
            type="text"
            placeholder="Search subject..."
            value={search}
            onChange={(e) =>
              setSearch(e.target.value)
            }
            className="
            w-full
            pl-12
            pr-4
            py-3
            rounded-xl
            border
            focus:ring-2
            focus:ring-blue-400
            outline-none
            "
          />

        </div>

      </div>

      {/* History Cards */}

      <div className="space-y-6">

        {filteredHistory.map((quiz) => {

          const percentage = Math.round(
            (quiz.score / quiz.total) * 100
          );

          return (

            <div
              key={quiz.id}
              className="
              bg-white
              rounded-3xl
              shadow-lg
              p-8
              hover:shadow-xl
              transition
              "
            >

              <div className="flex flex-col lg:flex-row justify-between gap-8">

                {/* Left */}

                <div>

                  <h2 className="text-2xl font-bold">

                    {quiz.subject} Quiz

                  </h2>

                  <p className="text-gray-500 mt-2">

                    📅 {quiz.date}

                  </p>

                  <div className="flex flex-wrap gap-3 mt-5">

                    <span className="bg-blue-100 text-blue-700 px-4 py-2 rounded-full text-sm">

                      {quiz.difficulty}

                    </span>

                    <span className="bg-purple-100 text-purple-700 px-4 py-2 rounded-full text-sm">

                      Score: {quiz.score}/{quiz.total}

                    </span>

                    <span
                      className={`px-4 py-2 rounded-full text-sm ${badgeColor(
                        percentage
                      )}`}
                    >

                      {percentage}% Accuracy

                    </span>

                  </div>

                </div>

                {/* Buttons */}

                <div className="flex flex-col sm:flex-row gap-4">

                  <Link
                    to="/result"
                    className="
                    flex
                    items-center
                    gap-2
                    bg-blue-600
                    hover:bg-blue-700
                    text-white
                    px-6
                    py-3
                    rounded-xl
                    transition
                    "
                  >

                    <FaEye />

                    View Result

                  </Link>

                  <Link
                    to="/quiz"
                    className="
                    flex
                    items-center
                    gap-2
                    bg-green-600
                    hover:bg-green-700
                    text-white
                    px-6
                    py-3
                    rounded-xl
                    transition
                    "
                  >

                    <FaRedo />

                    Retry Quiz

                  </Link>

                </div>

              </div>

            </div>

          );

        })}

        {filteredHistory.length === 0 && (

          <div className="bg-white rounded-3xl shadow-lg p-12 text-center">

            <h2 className="text-3xl font-bold">
              No Quiz Found
            </h2>

            <p className="text-gray-500 mt-4">
              Try searching with another subject.
            </p>

          </div>

        )}

      </div>

    </DashboardLayout>
  );
}

export default History;