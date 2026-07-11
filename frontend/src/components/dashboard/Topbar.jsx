import { Search, Bell, Moon, Sun } from "lucide-react";
import useAuth from "../../hooks/useAuth";
import useTheme from "../../hooks/useTheme";

function Topbar() {
  const { user } = useAuth();

  const { darkMode, toggleTheme } = useTheme();

  const today = new Date().toLocaleDateString("en-IN", {
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric",
  });

  return (
    <header
      className="
      bg-white
      dark:bg-slate-800
      rounded-2xl
      shadow-md
      p-5
      flex
      flex-col
      lg:flex-row
      lg:items-center
      lg:justify-between
      gap-4
      transition-colors
      duration-300
      "
    >
      {/* Left Side */}

      <div>

        <h1
          className="
          text-3xl
          font-bold
          text-slate-800
          dark:text-white
          "
        >
          Welcome back, {user?.name || "Student"} 👋
        </h1>

        <p
          className="
          text-gray-500
          dark:text-gray-300
          mt-1
          "
        >
          {today}
        </p>

      </div>

      {/* Right Side */}

      <div className="flex items-center gap-4">

        {/* Search */}

        <div className="relative">

          <Search
            className="absolute left-3 top-3 text-gray-400"
            size={18}
          />

          <input
            type="text"
            placeholder="Search..."
            className="
            w-64
            pl-10
            pr-4
            py-2.5
            rounded-xl
            border
            border-gray-300
            dark:border-slate-600
            bg-white
            dark:bg-slate-700
            dark:text-white
            focus:ring-2
            focus:ring-blue-500
            outline-none
            transition
            "
          />

        </div>

        {/* Notification */}

        <button
          className="
          p-3
          rounded-xl
          bg-slate-100
          dark:bg-slate-700
          hover:bg-slate-200
          dark:hover:bg-slate-600
          transition
          "
        >
          <Bell
            size={20}
            className="dark:text-white"
          />
        </button>

        {/* Dark Mode */}

        <button
          onClick={toggleTheme}
          className="
          p-3
          rounded-xl
          bg-slate-100
          dark:bg-slate-700
          hover:bg-slate-200
          dark:hover:bg-slate-600
          transition
          "
        >
          {darkMode ? (
            <Sun
              size={20}
              className="text-yellow-400"
            />
          ) : (
            <Moon size={20} />
          )}
        </button>

        {/* Avatar */}

        <div
          className="
          w-11
          h-11
          rounded-full
          bg-blue-600
          text-white
          flex
          items-center
          justify-center
          font-bold
          text-lg
          "
        >
          {user?.name?.charAt(0).toUpperCase() || "S"}
        </div>

      </div>

    </header>
  );
}

export default Topbar;