import {
  FaRobot,
  FaLightbulb,
  FaArrowTrendUp,
  FaTriangleExclamation,
} from "react-icons/fa6";

function StudyInsights() {
  const insights = [
    {
      icon: <FaArrowTrendUp />,
      title: "Strongest Subject",
      description: "DBMS has an average score of 92%. Keep it up!",
      color: "bg-green-100 text-green-600",
    },
    {
      icon: <FaTriangleExclamation />,
      title: "Needs Improvement",
      description: "Java accuracy is only 68%. Practice OOP and Collections.",
      color: "bg-red-100 text-red-600",
    },
    {
      icon: <FaLightbulb />,
      title: "Today's Recommendation",
      description:
        "Generate a Medium-level Python quiz with 15 questions.",
      color: "bg-yellow-100 text-yellow-600",
    },
    {
      icon: <FaRobot />,
      title: "AI Suggestion",
      description:
        "You're improving consistently. Maintain your 15-day study streak.",
      color: "bg-blue-100 text-blue-600",
    },
  ];

  return (
    <div className="bg-white rounded-3xl shadow-lg p-8">

      <h2 className="text-2xl font-bold mb-8">
        🤖 AI Study Insights
      </h2>

      <div className="space-y-6">

        {insights.map((item, index) => (

          <div
            key={index}
            className="flex items-start gap-5 border rounded-2xl p-5 hover:shadow-md transition"
          >

            <div
              className={`w-14 h-14 rounded-full flex items-center justify-center text-2xl ${item.color}`}
            >
              {item.icon}
            </div>

            <div>

              <h3 className="font-bold text-lg">
                {item.title}
              </h3>

              <p className="text-gray-600 mt-2">
                {item.description}
              </p>

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}

export default StudyInsights;