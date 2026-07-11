import AuthLayout from "../components/auth/AuthLayout";
import LoginForm from "../components/auth/LoginForm";

function Login() {
  return (
    <AuthLayout
      title="Welcome Back 👋"
      subtitle="Login to continue your AI-powered learning journey."
    >
      <LoginForm />
    </AuthLayout>
  );
}

export default Login;