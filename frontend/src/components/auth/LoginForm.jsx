import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { FaEye, FaEyeSlash } from "react-icons/fa";
import useAuth from "../../hooks/useAuth";

function LoginForm() {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [showPassword, setShowPassword] = useState(false);

  const [formData, setFormData] = useState({
    email: "",
    password: "",
    remember: false,
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;

    setFormData({
      ...formData,
      [name]: type === "checkbox" ? checked : value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Temporary fake login
    const fakeUser = {
      id: 1,
      name: "Demo User",
      email: formData.email,
    };

    login(fakeUser);

    navigate("/dashboard");
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white p-8 rounded-2xl shadow-xl w-full max-w-md"
    >
      <h2 className="text-3xl font-bold text-center mb-2">
        Welcome Back
      </h2>

      <p className="text-gray-500 text-center mb-8">
        Login to continue
      </p>

      <div className="mb-5">
        <label className="block mb-2 font-medium">
          Email
        </label>

        <input
          type="email"
          name="email"
          placeholder="Enter email"
          value={formData.email}
          onChange={handleChange}
          className="w-full border rounded-lg p-3"
          required
        />
      </div>

      <div className="mb-5">
        <label className="block mb-2 font-medium">
          Password
        </label>

        <div className="relative">

          <input
            type={showPassword ? "text" : "password"}
            name="password"
            placeholder="Enter password"
            value={formData.password}
            onChange={handleChange}
            className="w-full border rounded-lg p-3 pr-12"
            required
          />

          <button
            type="button"
            className="absolute right-4 top-4"
            onClick={() => setShowPassword(!showPassword)}
          >
            {showPassword ? <FaEyeSlash /> : <FaEye />}
          </button>

        </div>
      </div>

      <div className="flex justify-between items-center mb-6">

        <label className="flex items-center gap-2">

          <input
            type="checkbox"
            name="remember"
            checked={formData.remember}
            onChange={handleChange}
          />

          Remember Me

        </label>

        <Link
          to="/forgot-password"
          className="text-blue-600"
        >
          Forgot Password?
        </Link>

      </div>

      <button
        className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700"
      >
        Login
      </button>

      <p className="text-center mt-6">

        Don't have an account?

        <Link
          to="/signup"
          className="text-blue-600 ml-2"
        >
          Sign Up
        </Link>

      </p>

    </form>
  );
}

export default LoginForm;