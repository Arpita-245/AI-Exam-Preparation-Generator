import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

function PerformanceChart() {

  const data = [
    { day: "Mon", score: 60 },
    { day: "Tue", score: 72 },
    { day: "Wed", score: 80 },
    { day: "Thu", score: 74 },
    { day: "Fri", score: 90 },
    { day: "Sat", score: 95 },
    { day: "Sun", score: 88 },
  ];

  return (

    <div className="bg-white rounded-3xl shadow-lg p-8">

      <h2 className="text-2xl font-bold mb-6">

        Weekly Performance

      </h2>

      <ResponsiveContainer width="100%" height={320}>

        <LineChart data={data}>

          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="day" />

          <YAxis />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="score"
            stroke="#2563eb"
            strokeWidth={4}
          />

        </LineChart>

      </ResponsiveContainer>

    </div>

  );
}

export default PerformanceChart;