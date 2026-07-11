import AuthLayout from "../components/auth/AuthLayout";
import SignupForm from "../components/auth/SignupForm";

function Signup() {
  return (
    <AuthLayout
      title="Create Your Account 🚀"
      subtitle="Join ExamAI and start preparing smarter with AI-powered learning."
    >
      <SignupForm />
    </AuthLayout>
  );
}

export default Signup;