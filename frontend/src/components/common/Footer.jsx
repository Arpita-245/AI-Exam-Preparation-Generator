import { Link } from "react-router-dom";
import {
  FaGraduationCap,
  FaGithub,
  FaLinkedin,
  FaEnvelope,
  FaArrowUp,
} from "react-icons/fa";

function Footer() {
  const scrollTop = () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  };

  return (
    <footer className="bg-slate-950 text-white">

      <div className="max-w-7xl mx-auto px-6 py-20">

        <div className="grid lg:grid-cols-4 md:grid-cols-2 gap-12">

          {/* Brand */}

          <div>

            <div className="flex items-center gap-3 mb-6">

              <div className="w-12 h-12 rounded-xl bg-blue-600 flex items-center justify-center">
                <FaGraduationCap size={24} />
              </div>

              <div>

                <h2 className="text-2xl font-bold">
                  ExamAI
                </h2>

                <p className="text-gray-400 text-sm">
                  AI Exam Preparation
                </p>

              </div>

            </div>

            <p className="text-gray-400 leading-7">
              AI-powered platform that helps students
              upload notes, generate questions,
              attempt quizzes and track progress.
            </p>

          </div>

          {/* Quick Links */}

          <div>

            <h3 className="text-lg font-semibold mb-5">
              Quick Links
            </h3>

            <ul className="space-y-3 text-gray-400">

              <li>
                <Link
                  className="hover:text-white"
                  to="/"
                >
                  Home
                </Link>
              </li>

              <li>
                <Link
                  className="hover:text-white"
                  to="/login"
                >
                  Login
                </Link>
              </li>

              <li>
                <Link
                  className="hover:text-white"
                  to="/signup"
                >
                  Signup
                </Link>
              </li>

            </ul>

          </div>

          {/* Features */}

          <div>

            <h3 className="text-lg font-semibold mb-5">
              Features
            </h3>

            <ul className="space-y-3 text-gray-400">

              <li>Upload Notes</li>

              <li>AI Question Generator</li>

              <li>Practice Quiz</li>

              <li>Analytics</li>

            </ul>

          </div>

          {/* Contact */}

          <div>

            <h3 className="text-lg font-semibold mb-5">
              Contact
            </h3>

            <div className="space-y-4">

              <div className="flex items-center gap-3 text-gray-400">

                <FaEnvelope />

                support@examai.com

              </div>

              <div className="flex gap-4 mt-5">

                <a href="#">
                  <FaGithub
                    className="text-2xl hover:text-blue-400"
                  />
                </a>

                <a href="#">
                  <FaLinkedin
                    className="text-2xl hover:text-blue-400"
                  />
                </a>

              </div>

            </div>

          </div>

        </div>

        {/* Divider */}

        <div className="border-t border-slate-800 mt-16 pt-8 flex flex-col md:flex-row justify-between items-center gap-5">

          <p className="text-gray-500 text-center">
            © 2026 ExamAI. All Rights Reserved.
          </p>

          <button
            onClick={scrollTop}
            className="bg-blue-600 hover:bg-blue-700 p-3 rounded-full transition"
          >
            <FaArrowUp />
          </button>

        </div>

      </div>

    </footer>
  );
}

export default Footer;