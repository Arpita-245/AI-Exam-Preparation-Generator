import {
  FaCheckCircle,
  FaSpinner,
} from "react-icons/fa";

function UploadProgress({ progress }) {
  if (progress === 0) return null;

  const completed = progress === 100;

  return (
    <div
      className="
      bg-white
      rounded-3xl
      shadow-lg
      mt-8
      p-8
      "
    >
      <div className="flex justify-between items-center mb-5">

        <h2 className="text-2xl font-bold">
          Upload Progress
        </h2>

        {completed ? (
          <div className="flex items-center gap-2 text-green-600">
            <FaCheckCircle />
            Completed
          </div>
        ) : (
          <div className="flex items-center gap-2 text-blue-600">
            <FaSpinner className="animate-spin" />
            Uploading...
          </div>
        )}

      </div>

      <div className="w-full bg-gray-200 rounded-full h-4 overflow-hidden">

        <div
          className="
          bg-gradient-to-r
          from-blue-500
          to-cyan-500
          h-4
          rounded-full
          transition-all
          duration-300
          "
          style={{
            width: `${progress}%`,
          }}
        />

      </div>

      <div className="flex justify-between mt-4">

        <span className="text-gray-500">
          {progress}% Complete
        </span>

        <span className="font-semibold">
          {completed ? "Upload Finished" : "Uploading"}
        </span>

      </div>

    </div>
  );
}

export default UploadProgress;