import { useState } from "react";

function ForgotPassword() {
  const [email, setEmail] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    console.log(email);

    alert("Password reset link will be sent after backend integration.");
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white shadow-xl rounded-2xl p-8 w-full max-w-md"
    >
      <h2 className="text-3xl font-bold text-center mb-3">
        Forgot Password
      </h2>

      <p className="text-gray-500 text-center mb-8">
        Enter your registered email address.
      </p>

      <label className="block mb-2">
        Email
      </label>

      <input
        type="email"
        className="w-full border rounded-lg p-3 mb-6"
        placeholder="abc@gmail.com"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />

      <button
        className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700"
      >
        Send Reset Link
      </button>

    </form>
  );
}

export default ForgotPassword;