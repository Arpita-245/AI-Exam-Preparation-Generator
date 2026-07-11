import {
  FaBook,
  FaBrain,
  FaCheckCircle,
  FaFire,
  FaChartLine,
} from "react-icons/fa";

const stats = [
  {
    title: "Uploaded Notes",
    value: 12,
    icon: <FaBook />,
    color: "bg-blue-100 text-blue-700",
  },
  {
    title: "Generated Quizzes",
    value: 18,
    icon: <FaBrain />,
    color: "bg-purple-100 text-purple-700",
  },
  {
    title: "Questions Solved",
    value: 450,
    icon: <FaCheckCircle />,
    color: "bg-green-100 text-green-700",
  },
  {
    title: "Study Streak",
    value: "15 Days",
    icon: <FaFire />,
    color: "bg-orange-100 text-orange-700",
  },
  {
    title: "Average Accuracy",
    value: "87%",
    icon: <FaChartLine />,
    color: "bg-cyan-100 text-cyan-700",
  },
];

function ProfileStats() {
  return (
    <div className="grid md:grid-cols-2 xl:grid-cols-3 gap-6">

      {stats.map((item, index) => (

        <div
          key={index}
          className="bg-white rounded-3xl shadow-lg p-6"
        >

          <div
            className={`w-14 h-14 rounded-full flex items-center justify-center text-2xl ${item.color}`}
          >
            {item.icon}
          </div>

          <h3 className="mt-5 text-lg font-semibold">
            {item.title}
          </h3>

          <p className="text-3xl font-bold mt-2">
            {item.value}
          </p>

        </div>

      ))}

    </div>
  );
}

export default ProfileStats;