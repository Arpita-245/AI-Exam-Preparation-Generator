import useAuth from "../../hooks/useAuth";

function WelcomeBanner() {
  const { user } = useAuth();

  return (
    <div className="bg-blue-600 text-white rounded-2xl p-8">

      <h1 className="text-4xl font-bold">
        Welcome Back,
        {" "}
        {user?.name}
        👋
      </h1>

      <p className="mt-3 text-blue-100">
        Continue preparing for your exams using AI-powered quizzes.
      </p>

    </div>
  );
}

export default WelcomeBanner;