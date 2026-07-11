import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import {
  User,
  Mail,
  Lock,
  Eye,
  EyeOff,
} from "lucide-react";

import Button from "../common/Button";
import Input from "../common/Input";
import useAuth from "../../hooks/useAuth";

function SignupForm() {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [showPassword, setShowPassword] = useState(false);
  const [showConfirm, setShowConfirm] = useState(false);

  const [loading, setLoading] = useState(false);

  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
    terms: false,
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;

    setForm({
      ...form,
      [name]: type === "checkbox" ? checked : value,
    });
  };

  const getStrength = () => {
    const password = form.password;

    let score = 0;

    if (password.length >= 8) score++;
    if (/[A-Z]/.test(password)) score++;
    if (/[0-9]/.test(password)) score++;
    if (/[^A-Za-z0-9]/.test(password)) score++;

    if (score <= 1) return { text: "Weak", color: "bg-red-500" };
    if (score === 2) return { text: "Medium", color: "bg-yellow-500" };
    if (score >= 3) return { text: "Strong", color: "bg-green-500" };
  };

  const strength = getStrength();

  const handleSubmit = (e) => {
    e.preventDefault();

    if (
      !form.name ||
      !form.email ||
      !form.password ||
      !form.confirmPassword
    ) {
      alert("Please fill all fields.");
      return;
    }

    if (form.password !== form.confirmPassword) {
      alert("Passwords do not match.");
      return;
    }

    if (!form.terms) {
      alert("Accept Terms & Conditions.");
      return;
    }

    setLoading(true);

    setTimeout(() => {
      login({
        name: form.name,
        email: form.email,
      });

      navigate("/dashboard");
    }, 1500);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-5">

      <div className="relative">
        <User
          className="absolute left-4 top-11 text-gray-400"
          size={18}
        />

        <Input
          label="Full Name"
          name="name"
          placeholder="John Doe"
          className="pl-12"
          value={form.name}
          onChange={handleChange}
        />
      </div>

      <div className="relative">
        <Mail
          className="absolute left-4 top-11 text-gray-400"
          size={18}
        />

        <Input
          label="Email"
          name="email"
          type="email"
          placeholder="example@gmail.com"
          className="pl-12"
          value={form.email}
          onChange={handleChange}
        />
      </div>

      <div className="relative">
        <Lock
          className="absolute left-4 top-11 text-gray-400"
          size={18}
        />

        <Input
          label="Password"
          type={showPassword ? "text" : "password"}
          name="password"
          className="pl-12 pr-12"
          value={form.password}
          onChange={handleChange}
        />

        <button
          type="button"
          onClick={() => setShowPassword(!showPassword)}
          className="absolute right-4 top-11"
        >
          {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
        </button>
      </div>

      <div className="relative">
        <Lock
          className="absolute left-4 top-11 text-gray-400"
          size={18}
        />

        <Input
          label="Confirm Password"
          type={showConfirm ? "text" : "password"}
          name="confirmPassword"
          className="pl-12 pr-12"
          value={form.confirmPassword}
          onChange={handleChange}
        />

        <button
          type="button"
          onClick={() => setShowConfirm(!showConfirm)}
          className="absolute right-4 top-11"
        >
          {showConfirm ? <EyeOff size={18} /> : <Eye size={18} />}
        </button>
      </div>

      <div>
        <p className="text-sm mb-2">
          Password Strength:
          <span className="font-semibold ml-2">
            {strength.text}
          </span>
        </p>

        <div className="h-2 rounded-full bg-gray-200">
          <div
            className={`${strength.color} h-2 rounded-full transition-all`}
            style={{
              width:
                strength.text === "Weak"
                  ? "33%"
                  : strength.text === "Medium"
                  ? "66%"
                  : "100%",
            }}
          />
        </div>
      </div>

      <label className="flex items-center gap-2 text-sm">
        <input
          type="checkbox"
          name="terms"
          checked={form.terms}
          onChange={handleChange}
        />

        I accept Terms & Conditions
      </label>

      <Button type="submit" className="w-full">
        {loading ? "Creating Account..." : "Create Account"}
      </Button>

      <p className="text-center text-sm">
        Already have an account?
        <Link
          to="/login"
          className="ml-2 text-blue-600 font-semibold"
        >
          Login
        </Link>
      </p>
    </form>
  );
}

export default SignupForm;