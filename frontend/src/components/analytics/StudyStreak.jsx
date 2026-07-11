import {
  FaFire,
  FaCalendarCheck,
  FaTrophy,
  FaBullseye,
} from "react-icons/fa";

function StudyStreak() {
  const stats = [
    {
      title: "Current Streak",
      value: "15 Days",
      icon: <FaFire />,
      color: "bg-orange-100 text-orange-600",
    },
    {
      title: "Longest Streak",
      value: "28 Days",
      icon: <FaTrophy />,
      color: "bg-yellow-100 text-yellow-600",
    },
    {
      title: "Study Days",
      value: "48",
      icon: <FaCalendarCheck />,
      color: "bg-green-100 text-green-600",
    },
    {
      title: "Weekly Goal",
      value: "5 / 7",
      icon: <FaBullseye />,
      color: "bg-blue-100 text-blue-600",
    },
  ];

  return (
    <div className="bg-white rounded-3xl shadow-lg p-8">

      <h2 className="text-2xl font-bold mb-8">
        🔥 Study Streak
      </h2>

      <div className="grid md:grid-cols-2 gap-6">

        {stats.map((item, index) => (

          <div
            key={index}
            className="flex items-center gap-5 border rounded-2xl p-5 hover:shadow-md transition"
          >

            <div
              className={`w-14 h-14 rounded-full flex items-center justify-center text-2xl ${item.color}`}
            >
              {item.icon}
            </div>

            <div>

              <p className="text-gray-500">
                {item.title}
              </p>

              <h3 className="text-2xl font-bold mt-1">
                {item.value}
              </h3>

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}

export default StudyStreak;