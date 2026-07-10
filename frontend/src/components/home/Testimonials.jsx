import { motion } from "framer-motion";
import { FaStar } from "react-icons/fa";

const testimonials = [
  {
    name: "Aarav Patel",
    role: "B.Sc. IT Student",
    review:
      "The AI-generated questions helped me prepare much faster for my semester exams. The quiz feature is excellent!",
    initials: "AP",
  },
  {
    name: "Priya Sharma",
    role: "Computer Science Student",
    review:
      "Uploading my notes and getting instant MCQs saved me hours of manual preparation. Highly recommended!",
    initials: "PS",
  },
  {
    name: "Rohan Mehta",
    role: "Engineering Student",
    review:
      "The dashboard and performance tracking helped me identify weak topics and improve consistently.",
    initials: "RM",
  },
];

function Testimonials() {
  return (
    <section className="py-24 bg-slate-50">
      <div className="max-w-7xl mx-auto px-6">

        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          transition={{ duration: 0.7 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <h2 className="text-5xl font-bold">
            What Students Say
          </h2>

          <p className="text-gray-600 mt-4 text-lg max-w-2xl mx-auto">
            Thousands of learners use ExamAI to prepare smarter and achieve better results.
          </p>
        </motion.div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {testimonials.map((item, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 60 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{
                duration: 0.6,
                delay: index * 0.15,
              }}
              viewport={{ once: true }}
              whileHover={{
                y: -8,
                scale: 1.02,
              }}
              className="bg-white rounded-3xl shadow-lg p-8 border border-gray-100"
            >
              <div className="flex items-center gap-4 mb-6">

                <div className="w-14 h-14 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold text-lg">
                  {item.initials}
                </div>

                <div>
                  <h3 className="font-bold text-lg">
                    {item.name}
                  </h3>

                  <p className="text-gray-500 text-sm">
                    {item.role}
                  </p>
                </div>

              </div>

              <div className="flex gap-1 text-yellow-400 mb-4">
                {[...Array(5)].map((_, i) => (
                  <FaStar key={i} />
                ))}
              </div>

              <p className="text-gray-600 leading-7">
                "{item.review}"
              </p>
            </motion.div>
          ))}
        </div>

      </div>
    </section>
  );
}

export default Testimonials;