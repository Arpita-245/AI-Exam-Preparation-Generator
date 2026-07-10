import { useState } from "react";
import { Link } from "react-router-dom";
import { FaEye, FaEyeSlash } from "react-icons/fa";

function SignupForm() {
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirm, setShowConfirm] = useState(false);

  const [formData, setFormData] = useState({
    fullName: "",
    email: "",
    password: "",
    confirmPassword: "",
    agree: false,
  });

  const handleChange = (e) => {
    const { name, value, checked, type } = e.target;

    setFormData({
      ...formData,
      [name]: type === "checkbox" ? checked : value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (formData.password !== formData.confirmPassword) {
      alert("Passwords do not match");
      return;
    }

    console.log(formData);

    // Backend API later
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white p-8 rounded-2xl shadow-xl w-full max-w-md"
    >
      <h2 className="text-3xl font-bold text-center mb-2">
        Create Account
      </h2>

      <p className="text-gray-500 text-center mb-8">
        Sign up to get started
      </p>

      <div className="mb-5">
        <label className="block mb-2">Full Name</label>

        <input
          type="text"
          name="fullName"
          placeholder="John Doe"
          value={formData.fullName}
          onChange={handleChange}
          className="w-full border rounded-lg p-3"
          required
        />
      </div>

      <div className="mb-5">
        <label className="block mb-2">Email</label>

        <input
          type="email"
          name="email"
          placeholder="abc@gmail.com"
          value={formData.email}
          onChange={handleChange}
          className="w-full border rounded-lg p-3"
          required
        />
      </div>

      <div className="mb-5">
        <label className="block mb-2">
          Password
        </label>

        <div className="relative">

          <input
            type={showPassword ? "text" : "password"}
            name="password"
            value={formData.password}
            onChange={handleChange}
            className="w-full border rounded-lg p-3 pr-12"
            required
          />

          <button
            type="button"
            onClick={() => setShowPassword(!showPassword)}
            className="absolute right-4 top-4"
          >
            {showPassword ? <FaEyeSlash /> : <FaEye />}
          </button>

        </div>
      </div>

      <div className="mb-5">
        <label className="block mb-2">
          Confirm Password
        </label>

        <div className="relative">

          <input
            type={showConfirm ? "text" : "password"}
            name="confirmPassword"
            value={formData.confirmPassword}
            onChange={handleChange}
            className="w-full border rounded-lg p-3 pr-12"
            required
          />

          <button
            type="button"
            onClick={() => setShowConfirm(!showConfirm)}
            className="absolute right-4 top-4"
          >
            {showConfirm ? <FaEyeSlash /> : <FaEye />}
          </button>

        </div>
      </div>

      <div className="flex items-center gap-2 mb-6">

        <input
          type="checkbox"
          name="agree"
          checked={formData.agree}
          onChange={handleChange}
          required
        />

        I agree to Terms & Conditions

      </div>

      <button
        className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700"
      >
        Create Account
      </button>

      <p className="text-center mt-6">

        Already have an account?

        <Link
          to="/login"
          className="text-blue-600 ml-2"
        >
          Login
        </Link>

      </p>

    </form>
  );
}

export default SignupForm;