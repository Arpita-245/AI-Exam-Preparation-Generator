import DashboardLayout from "../layouts/DashboardLayout";

import ProfileCard from "../components/profile/ProfileCard";
import ProfileStats from "../components/profile/ProfileStats";
import AchievementCard from "../components/profile/AchievementCard";
import ChangePassword from "../components/profile/ChangePassword";

function Profile() {

  const user = {
    name: "John Doe",
    email: "john@gmail.com",
  };

  return (

    <DashboardLayout>

      <div className="max-w-7xl mx-auto">

        {/* Heading */}

        <div className="mb-10">

          <h1 className="text-4xl font-bold">

            My Profile

          </h1>

          <p className="text-gray-500 mt-2">

            View your learning progress and account details.

          </p>

        </div>

        {/* Profile */}

        <ProfileCard user={user} />

        {/* Statistics */}

        <div className="mt-10">

          <ProfileStats />

        </div>

        {/* Achievements */}

        <div className="mt-10">

          <AchievementCard />

        </div>

        {/* Password */}

        <div className="mt-10">

          <ChangePassword />

        </div>

      </div>

    </DashboardLayout>

  );

}

export default Profile;