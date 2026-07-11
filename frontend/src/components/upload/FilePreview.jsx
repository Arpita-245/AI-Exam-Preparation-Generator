import {
  FaFileAlt,
  FaTrashAlt,
  FaCheckCircle,
} from "react-icons/fa";

function FilePreview({ file, removeFile }) {
  if (!file) return null;

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
      <h2 className="text-2xl font-bold mb-6">
        Selected File
      </h2>

      <div className="flex items-center justify-between flex-wrap gap-6">

        <div className="flex items-center gap-5">

          <div className="bg-blue-100 p-5 rounded-2xl">
            <FaFileAlt
              className="text-blue-600"
              size={35}
            />
          </div>

          <div>

            <h3 className="font-semibold text-lg">
              {file.name}
            </h3>

            <p className="text-gray-500">
              {(file.size / 1024 / 1024).toFixed(2)} MB
            </p>

            <div className="flex items-center gap-2 mt-2 text-green-600">

              <FaCheckCircle />

              Ready to upload

            </div>

          </div>

        </div>

        <button
          onClick={removeFile}
          className="
            flex
            items-center
            gap-2
            bg-red-600
            hover:bg-red-700
            text-white
            px-5
            py-3
            rounded-xl
            transition
          "
        >
          <FaTrashAlt />

          Remove
        </button>

      </div>

    </div>
  );
}

export default FilePreview;