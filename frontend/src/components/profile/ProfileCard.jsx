import useAuth from "../../hooks/useAuth";

function ProfileCard() {
  const { user } = useAuth();

  return (
    <div className="bg-white rounded-xl shadow-lg p-8">

      <div className="flex flex-col items-center">

        <img
          src="https://ui-avatars.com/api/?name=Demo+User&background=2563eb&color=fff&size=150"
          alt="avatar"
          className="rounded-full w-32 h-32"
        />

        <h2 className="text-3xl font-bold mt-5">
          {user?.name}
        </h2>

        <p className="text-gray-500 mt-2">
          {user?.email}
        </p>

      </div>

      <div className="grid md:grid-cols-2 gap-6 mt-10">

        <div>

          <label className="font-medium">
            College
          </label>

          <input
            className="w-full border rounded-lg p-3 mt-2"
            defaultValue="ABC College"
          />

        </div>

        <div>

          <label className="font-medium">
            Course
          </label>

          <input
            className="w-full border rounded-lg p-3 mt-2"
            defaultValue="B.Sc IT"
          />

        </div>

        <div>

          <label className="font-medium">
            Semester
          </label>

          <input
            className="w-full border rounded-lg p-3 mt-2"
            defaultValue="Semester 5"
          />

        </div>

      </div>

    </div>
  );
}

export default ProfileCard;