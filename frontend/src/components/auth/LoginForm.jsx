import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import {
  Eye,
  EyeOff,
  Mail,
  Lock,
} from "lucide-react";

import Button from "../common/Button";
import Input from "../common/Input";
import useAuth from "../../hooks/useAuth";

function LoginForm() {

  const navigate = useNavigate();

  const { login } = useAuth();

  const [showPassword, setShowPassword] = useState(false);

  const [loading, setLoading] = useState(false);

  const [form, setForm] = useState({
    email: "",
    password: "",
    remember: false,
  });

  const handleChange = (e) => {

    const { name, value, type, checked } = e.target;

    setForm({
      ...form,
      [name]:
        type === "checkbox"
          ? checked
          : value,
    });

  };

  const handleSubmit = (e) => {

    e.preventDefault();

    if (!form.email || !form.password) {

      alert("Please fill all fields.");

      return;

    }

    setLoading(true);

    setTimeout(() => {

      login({

        name: "Student",

        email: form.email,

      });

      navigate("/dashboard");

    },1500);

  };

  return (

    <form
      onSubmit={handleSubmit}
      className="space-y-6"
    >

      <div>

        <label className="font-medium">

          Email

        </label>

        <div className="relative mt-2">

          <Mail
            size={18}
            className="absolute left-4 top-4 text-gray-400"
          />

          <Input

            type="email"

            name="email"

            placeholder="Enter your email"

            value={form.email}

            onChange={handleChange}

            className="pl-12"

          />

        </div>

      </div>

      <div>

        <label className="font-medium">

          Password

        </label>

        <div className="relative mt-2">

          <Lock
            size={18}
            className="absolute left-4 top-4 text-gray-400"
          />

          <Input

            type={
              showPassword
                ? "text"
                : "password"
            }

            name="password"

            placeholder="Enter your password"

            value={form.password}

            onChange={handleChange}

            className="pl-12 pr-12"

          />

          <button

            type="button"

            className="absolute right-4 top-4"

            onClick={() =>
              setShowPassword(
                !showPassword
              )
            }

          >

            {showPassword
              ? <EyeOff size={18}/>
              : <Eye size={18}/>}

          </button>

        </div>

      </div>

      <div className="flex justify-between items-center">

        <label className="flex items-center gap-2">

          <input

            type="checkbox"

            name="remember"

            checked={form.remember}

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

      <Button
        type="submit"
        className="w-full"
      >

        {loading
          ? "Logging in..."
          : "Login"}

      </Button>

      <p className="text-center">

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