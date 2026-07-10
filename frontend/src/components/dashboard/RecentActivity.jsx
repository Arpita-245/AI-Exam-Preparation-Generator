function RecentActivity() {

  const activities = [
    "Uploaded DBMS Notes",
    "Generated Python Quiz",
    "Completed AI Mock Test",
    "Viewed Quiz History",
  ];

  return (
    <div className="bg-white rounded-xl shadow p-6 mt-8">

      <h2 className="text-2xl font-bold mb-6">
        Recent Activity
      </h2>

      <ul className="space-y-4">

        {activities.map((activity, index) => (

          <li
            key={index}
            className="border-b pb-3"
          >
            {activity}
          </li>

        ))}

      </ul>

    </div>
  );
}

export default RecentActivity;