import DashboardLayout from "../layouts/DashboardLayout";
import { Link } from "react-router-dom";

function History() {

  const history = [
    {
      id: 1,
      subject: "DBMS",
      score: 8,
      total: 10,
      date: "10 July 2026",
    },
    {
      id: 2,
      subject: "Python",
      score: 10,
      total: 10,
      date: "09 July 2026",
    },
    {
      id: 3,
      subject: "Java",
      score: 7,
      total: 10,
      date: "08 July 2026",
    },
  ];

  return (
    <DashboardLayout>

      <h1 className="text-4xl font-bold mb-10">

        Quiz History

      </h1>

      <div className="space-y-6">

        {history.map((quiz) => (

          <div
            key={quiz.id}
            className="bg-white rounded-xl shadow p-6"
          >

            <div className="flex justify-between">

              <div>

                <h2 className="text-2xl font-bold">

                  {quiz.subject} Quiz

                </h2>

                <p className="mt-3">

                  Date : {quiz.date}

                </p>

                <p>

                  Score : {quiz.score}/{quiz.total}

                </p>

                <p>

                  Accuracy :

                  {" "}

                  {Math.round(
                    (quiz.score / quiz.total) * 100
                  )}

                  %

                </p>

              </div>

              <div>

                <Link
                  to="/result"
                  className="bg-blue-600 text-white px-5 py-3 rounded-lg"
                >
                  View Result
                </Link>

              </div>

            </div>

          </div>

        ))}

      </div>

    </DashboardLayout>
  );
}

export default History;