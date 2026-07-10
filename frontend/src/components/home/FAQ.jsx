import { useState } from "react";
import { FaPlus, FaMinus } from "react-icons/fa";
import { motion, AnimatePresence } from "framer-motion";

const faqs = [
  {
    question: "How does the AI Question Generator work?",
    answer:
      "The AI analyzes your uploaded study material and automatically generates MCQs, subjective questions, and quizzes based on the content.",
  },
  {
    question: "Which file formats can I upload?",
    answer:
      "You can upload PDF, DOCX, TXT, and images. The backend will extract the text before generating questions.",
  },
  {
    question: "Can I attempt quizzes multiple times?",
    answer:
      "Yes. You can generate new quizzes and retake previous ones to improve your understanding.",
  },
  {
    question: "Will my progress be saved?",
    answer:
      "Yes. After backend integration, your quiz history, scores, and uploaded notes will be securely stored in your account.",
  },
];

function FAQ() {
  const [activeIndex, setActiveIndex] = useState(null);

  const toggleFAQ = (index) => {
    setActiveIndex(activeIndex === index ? null : index);
  };

  return (
    <section id="faq" className="py-24 bg-white">
      <div className="max-w-4xl mx-auto px-6">

        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          transition={{ duration: 0.7 }}
          viewport={{ once: true }}
          className="text-center mb-14"
        >
          <h2 className="text-5xl font-bold">
            Frequently Asked Questions
          </h2>

          <p className="text-gray-600 mt-4 text-lg">
            Find answers to the most common questions about ExamAI.
          </p>
        </motion.div>

        <div className="space-y-5">

          {faqs.map((faq, index) => (
            <div
              key={index}
              className="border border-gray-200 rounded-2xl overflow-hidden shadow-sm"
            >
              <button
                onClick={() => toggleFAQ(index)}
                className="w-full flex justify-between items-center p-6 text-left hover:bg-gray-50 transition"
              >
                <span className="font-semibold text-lg">
                  {faq.question}
                </span>

                {activeIndex === index ? (
                  <FaMinus className="text-blue-600" />
                ) : (
                  <FaPlus className="text-blue-600" />
                )}
              </button>

              <AnimatePresence>
                {activeIndex === index && (
                  <motion.div
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: "auto", opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    transition={{ duration: 0.3 }}
                  >
                    <div className="px-6 pb-6 text-gray-600 leading-7">
                      {faq.answer}
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>

            </div>
          ))}

        </div>

      </div>
    </section>
  );
}

export default FAQ;