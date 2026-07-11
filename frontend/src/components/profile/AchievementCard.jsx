const achievements = [
  "🏅 First Quiz Completed",
  "🔥 7 Day Study Streak",
  "💯 Perfect Score",
  "📚 Quiz Master",
];

function AchievementCard() {
  return (
    <div className="bg-white rounded-3xl shadow-lg p-8">

      <h2 className="text-2xl font-bold mb-6">
        Achievements
      </h2>

      <div className="space-y-4">

        {achievements.map((item, index) => (

          <div
            key={index}
            className="bg-slate-100 rounded-xl p-4"
          >
            {item}
          </div>

        ))}

      </div>

    </div>
  );
}

export default AchievementCard;