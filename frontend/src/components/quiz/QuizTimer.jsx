import { useEffect, useState } from "react";

function QuizTimer() {
  const [time, setTime] = useState(900); //15 minutes

  useEffect(() => {
    const timer = setInterval(() => {
      setTime((prev) => {
        if (prev <= 1) {
          clearInterval(timer);
          return 0;
        }

        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  const minutes = Math.floor(time / 60);
  const seconds = time % 60;

  return (
    <div className="bg-red-100 text-red-700 px-5 py-3 rounded-lg font-bold">
      Time Left :
      {" "}
      {minutes}:{seconds.toString().padStart(2, "0")}
    </div>
  );
}

export default QuizTimer;