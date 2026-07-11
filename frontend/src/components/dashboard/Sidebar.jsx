import { NavLink, useNavigate } from "react-router-dom";
import {
  FaHome,
  FaUpload,
  FaBrain,
  FaHistory,
  FaChartBar,
  FaUser,
  FaSignOutAlt,
} from "react-icons/fa";

import useAuth from "../../hooks/useAuth";

function Sidebar() {
  const { logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  const linkClass = ({ isActive }) =>
    `flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 ${
      isActive
        ? "bg-blue-600 text-white shadow-lg"
        : "text-gray-700 hover:bg-blue-100"
    }`;

  return (
    <aside className="w-72 min-h-screen bg-white shadow-xl p-6 flex flex-col justify-between flex-shrink-0">

      <div>

        <h1 className="text-3xl font-extrabold text-blue-600 mb-10">
          ExamAI
        </h1>

        <nav className="space-y-3">

          <NavLink to="/dashboard" className={linkClass}>
            <FaHome />
            Dashboard
          </NavLink>

          <NavLink to="/upload" className={linkClass}>
            <FaUpload />
            Upload Notes
          </NavLink>

          <NavLink to="/generate" className={linkClass}>
            <FaBrain />
            Generate Questions
          </NavLink>

          <NavLink to="/history" className={linkClass}>
            <FaHistory />
            History
          </NavLink>

          <NavLink to="/analytics" className={linkClass}>
            <FaChartBar />
            Analytics
          </NavLink>

          <NavLink to="/profile" className={linkClass}>
            <FaUser />
            Profile
          </NavLink>

        </nav>

      </div>

      <button
        onClick={handleLogout}
        className="bg-red-600 hover:bg-red-700 text-white py-3 rounded-xl transition-all flex items-center justify-center gap-3 font-semibold"
      >
        <FaSignOutAlt />
        Logout
      </button>

    </aside>
  );
}

export default Sidebar;