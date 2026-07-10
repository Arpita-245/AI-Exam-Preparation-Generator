import DashboardLayout from "../layouts/DashboardLayout";

import ProfileCard from "../components/profile/ProfileCard";
import ChangePassword from "../components/profile/ChangePassword";

function Profile() {
  return (
    <DashboardLayout>

      <h1 className="text-4xl font-bold mb-10">
        My Profile
      </h1>

      <ProfileCard />

      <ChangePassword />

    </DashboardLayout>
  );
}

export default Profile;