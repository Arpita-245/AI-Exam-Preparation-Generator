import Sidebar from "../components/dashboard/Sidebar";

function DashboardLayout({ children }) {
  return (
    <div className="flex min-h-screen bg-slate-100">

      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <main className="flex-1 p-6 lg:p-8 overflow-y-auto">

        {children}

      </main>

    </div>
  );
}

export default DashboardLayout;