import { Link } from "react-router-dom";
import { motion } from "framer-motion";
import Button from "../common/Button";

function CTA() {
  return (
    <section className="py-24 bg-gradient-to-r from-blue-600 via-indigo-600 to-violet-600">
      <div className="max-w-5xl mx-auto px-6 text-center text-white">

        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          whileInView={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.7 }}
          viewport={{ once: true }}
        >
          <span className="inline-block px-4 py-2 bg-white/20 rounded-full text-sm font-semibold mb-6">
            🚀 Start Your AI Learning Journey
          </span>

          <h2 className="text-5xl font-bold leading-tight">
            Ready to Prepare Smarter?
          </h2>

          <p className="mt-6 text-lg text-blue-100 max-w-2xl mx-auto">
            Upload your notes, generate AI-powered questions, take quizzes,
            and track your progress—all in one place.
          </p>

          <div className="mt-10 flex flex-wrap justify-center gap-4">

            <Link to="/signup">
              <Button className="bg-white text-blue-600 hover:bg-gray-100">
                Create Free Account
              </Button>
            </Link>

            <Link to="/login">
              <Button
                variant="outline"
                className="border-white text-white hover:bg-white hover:text-blue-600"
              >
                Login
              </Button>
            </Link>

          </div>

        </motion.div>
      </div>
    </section>
  );
}

export default CTA;