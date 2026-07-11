import DashboardLayout from "../layouts/DashboardLayout";
import SubjectPieChart from "../components/analytics/SubjectPieChart";
import AnalyticsCards from "../components/analytics/AnalyticsCards";
import PerformanceChart from "../components/analytics/PerformanceChart";
import StudyStreak from "../components/analytics/StudyStreak";
import StudyInsights from "../components/analytics/StudyInsights";
function Analytics() {
  return (
    <DashboardLayout>

      <h1 className="text-4xl font-bold mb-8">

        📊 Study Analytics

      </h1>

      <AnalyticsCards />

      <div className="grid lg:grid-cols-2 gap-8 mt-10">

        <PerformanceChart />
        <SubjectPieChart />
      </div>
      <div className="mt-10">
        <StudyStreak />
      </div>
      <div className="mt-10">
        <StudyInsights />
      </div>
    </DashboardLayout>
  );
}

export default Analytics;