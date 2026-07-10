import { NavLink, useNavigate } from "react-router-dom";
import useAuth from "../../hooks/useAuth";

function Sidebar() {
  const { logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  const linkClass = ({ isActive }) =>
    `block px-4 py-3 rounded-lg transition ${
      isActive
        ? "bg-blue-600 text-white"
        : "text-gray-700 hover:bg-blue-100"
    }`;

  return (
    <aside className="w-64 bg-white shadow-lg min-h-screen p-6">

      <h1 className="text-3xl font-bold text-blue-600 mb-10">
        ExamAI
      </h1>

      <nav className="space-y-2">

        <NavLink to="/dashboard" className={linkClass}>
          Dashboard
        </NavLink>

        <NavLink to="/upload" className={linkClass}>
          Upload Notes
        </NavLink>

        <NavLink to="/generate" className={linkClass}>
          Generate Questions
        </NavLink>

        <NavLink to="/history" className={linkClass}>
          History
        </NavLink>

        <NavLink to="/profile" className={linkClass}>
          Profile
        </NavLink>

      </nav>

      <button
        onClick={handleLogout}
        className="mt-10 w-full bg-red-600 text-white py-3 rounded-lg hover:bg-red-700"
      >
        Logout
      </button>

    </aside>
  );
}

export default Sidebar;