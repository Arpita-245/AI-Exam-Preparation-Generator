import { GraduationCap } from "lucide-react";

function AuthLayout({ title, subtitle, children }) {
  return (
    <div className="min-h-screen grid lg:grid-cols-2 bg-slate-50">

      {/* Left Side */}
      <div className="hidden lg:flex flex-col justify-center bg-gradient-to-br from-blue-700 via-indigo-700 to-violet-700 text-white p-16">

        <div className="flex items-center gap-4 mb-8">
          <div className="bg-white/20 p-4 rounded-2xl">
            <GraduationCap size={42} />
          </div>

          <div>
            <h1 className="text-4xl font-bold">
              ExamAI
            </h1>

            <p className="text-blue-100">
              AI Exam Preparation Platform
            </p>
          </div>
        </div>

        <h2 className="text-5xl font-bold leading-tight mb-6">
          Prepare Smarter,
          <br />
          Score Better.
        </h2>

        <p className="text-lg text-blue-100 leading-8 max-w-md">
          Upload notes, generate AI-powered questions,
          attempt quizzes and track your progress
          from one beautiful dashboard.
        </p>

      </div>

      {/* Right Side */}
      <div className="flex items-center justify-center px-6 py-12">

        <div className="w-full max-w-md bg-white rounded-3xl shadow-2xl p-8">

          <h2 className="text-3xl font-bold text-slate-900">
            {title}
          </h2>

          <p className="text-gray-500 mt-2 mb-8">
            {subtitle}
          </p>

          {children}

        </div>

      </div>

    </div>
  );
}

export default AuthLayout;