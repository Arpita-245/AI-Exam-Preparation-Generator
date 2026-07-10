function ChangePassword() {
  return (
    <div className="bg-white rounded-xl shadow-lg p-8 mt-10">

      <h2 className="text-2xl font-bold mb-6">
        Change Password
      </h2>

      <div className="space-y-5">

        <input
          type="password"
          placeholder="Current Password"
          className="w-full border rounded-lg p-3"
        />

        <input
          type="password"
          placeholder="New Password"
          className="w-full border rounded-lg p-3"
        />

        <input
          type="password"
          placeholder="Confirm Password"
          className="w-full border rounded-lg p-3"
        />

      </div>

      <button
        className="mt-8 bg-blue-600 text-white px-8 py-3 rounded-lg"
      >
        Save Changes
      </button>

    </div>
  );
}

export default ChangePassword;