import { Link } from "react-router-dom";

function CTA() {
  return (
    <section className="bg-linear-to-r from-blue-600 to-indigo-700 py-24">

      <div className="max-w-4xl mx-auto text-center px-6">

        <h2 className="text-5xl font-bold text-white mb-6">
          Ready to Ace Your Exams?
        </h2>

        <p className="text-blue-100 text-lg mb-10">
          Upload your study notes, generate AI-powered
          questions, practice quizzes and track your
          learning progress.
        </p>

        <div className="flex flex-col sm:flex-row justify-center gap-6">

          <Link to="/signup">
            <button className="bg-white text-blue-600 font-semibold px-8 py-3 rounded-lg hover:bg-gray-100 transition">
              Get Started
            </button>
          </Link>

          <Link to="/login">
            <button className="border border-white text-white px-8 py-3 rounded-lg hover:bg-white hover:text-blue-600 transition">
              Login
            </button>
          </Link>

        </div>

      </div>

    </section>
  );
}

export default CTA;