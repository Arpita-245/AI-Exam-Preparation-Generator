import {
  FaBook,
  FaQuestionCircle,
  FaBullseye,
  FaClock,
} from "react-icons/fa";

function AnalyticsCards() {
  const cards = [
    {
      title: "Uploaded Notes",
      value: 12,
      icon: <FaBook />,
      color: "from-blue-500 to-indigo-600",
    },
    {
      title: "Generated Quizzes",
      value: 18,
      icon: <FaQuestionCircle />,
      color: "from-purple-500 to-pink-600",
    },
    {
      title: "Average Accuracy",
      value: "87%",
      icon: <FaBullseye />,
      color: "from-green-500 to-emerald-600",
    },
    {
      title: "Study Hours",
      value: "42",
      icon: <FaClock />,
      color: "from-orange-500 to-red-600",
    },
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

      {cards.map((card, index) => (

        <div
          key={index}
          className={`bg-gradient-to-r ${card.color} text-white rounded-3xl p-6 shadow-lg`}
        >
          <div className="flex justify-between items-center">

            <div>

              <p className="opacity-90">
                {card.title}
              </p>

              <h2 className="text-4xl font-bold mt-3">
                {card.value}
              </h2>

            </div>

            <div className="text-5xl opacity-80">

              {card.icon}

            </div>

          </div>

        </div>

      ))}

    </div>
  );
}

export default AnalyticsCards;