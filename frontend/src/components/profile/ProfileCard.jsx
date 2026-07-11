import { FaUserCircle } from "react-icons/fa";

function ProfileCard({ user }) {
  return (
    <div className="bg-white rounded-3xl shadow-lg p-8 text-center">

      <FaUserCircle
        className="mx-auto text-blue-600"
        size={120}
      />

      <h2 className="text-3xl font-bold mt-6">
        {user.name}
      </h2>

      <p className="text-gray-500 mt-2">
        {user.email}
      </p>

      <div className="mt-6">

        <span className="bg-blue-100 text-blue-700 px-5 py-2 rounded-full">

          AI Learner

        </span>

      </div>

    </div>
  );
}

export default ProfileCard;