import { Link } from "react-router-dom";

function Footer() {
  return (
    <footer className="bg-slate-900 text-white py-16">
      <div className="max-w-7xl mx-auto px-6 grid md:grid-cols-4 gap-10">

        <div>
          <h2 className="text-3xl font-bold mb-4">
            ExamAI
          </h2>

          <p className="text-gray-400">
            AI-powered Exam Preparation and Question Generator platform.
          </p>
        </div>

        <div>
          <h3 className="font-semibold mb-4">Quick Links</h3>

          <ul className="space-y-2">
            <li><Link to="/">Home</Link></li>
            <li><Link to="/login">Login</Link></li>
            <li><Link to="/signup">Signup</Link></li>
          </ul>
        </div>

        <div>
          <h3 className="font-semibold mb-4">Features</h3>

          <ul className="space-y-2">
            <li>Upload Notes</li>
            <li>Generate Questions</li>
            <li>Mock Quiz</li>
            <li>Progress Tracking</li>
          </ul>
        </div>

        <div>
          <h3 className="font-semibold mb-4">Contact</h3>

          <p className="text-gray-400">
            support@examai.com
          </p>

          <div className="mt-4 space-y-2 text-gray-400">
            <p>GitHub</p>
            <p>LinkedIn</p>
          </div>
        </div>

      </div>

      <div className="text-center text-gray-500 mt-12">
        © 2026 ExamAI. All Rights Reserved.
      </div>
    </footer>
  );
}

export default Footer;