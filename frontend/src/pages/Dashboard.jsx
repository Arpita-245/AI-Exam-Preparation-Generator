import DashboardLayout from "../layouts/DashboardLayout";
import WelcomeBanner from "../components/dashboard/WelcomeBanner";
import StatsCard from "../components/dashboard/StatsCard";
import RecentActivity from "../components/dashboard/RecentActivity";

function Dashboard() {
  return (
    <DashboardLayout>

      <WelcomeBanner />

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mt-8">

        <StatsCard
          title="Uploaded Notes"
          value="12"
        />

        <StatsCard
          title="Generated Quizzes"
          value="18"
        />

        <StatsCard
          title="Questions Solved"
          value="450"
        />

        <StatsCard
          title="Accuracy"
          value="87%"
        />

      </div>

      <RecentActivity />

    </DashboardLayout>
  );
}

export default Dashboard;