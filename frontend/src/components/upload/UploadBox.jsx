import { useRef } from "react";
import { FaCloudUploadAlt } from "react-icons/fa";

function UploadBox({ onFileSelect }) {
  const inputRef = useRef();

  const handleClick = () => {
    inputRef.current.click();
  };

  const handleChange = (e) => {
    if (e.target.files[0]) {
      onFileSelect(e.target.files[0]);
    }
  };

  return (
    <div
      onClick={handleClick}
      className="
        bg-white
        rounded-3xl
        shadow-lg
        border-2
        border-dashed
        border-blue-400
        hover:border-blue-600
        hover:shadow-xl
        transition-all
        duration-300
        cursor-pointer
        p-12
        text-center
      "
    >
      <div className="flex justify-center">
        <div className="bg-blue-100 p-6 rounded-full">
          <FaCloudUploadAlt
            size={60}
            className="text-blue-600"
          />
        </div>
      </div>

      <h2 className="text-3xl font-bold mt-6">
        Upload Study Notes
      </h2>

      <p className="text-gray-500 mt-3">
        Drag & Drop your files here
      </p>

      <p className="text-gray-400 mt-2">
        or click anywhere to browse
      </p>

      <button
        type="button"
        className="
          mt-8
          bg-blue-600
          hover:bg-blue-700
          text-white
          px-8
          py-3
          rounded-xl
          font-semibold
          transition
        "
      >
        Browse Files
      </button>

      <div className="mt-6 text-sm text-gray-500">
        Supported formats:
        <span className="font-semibold">
          {" "}PDF • DOC • DOCX • TXT
        </span>
      </div>

      <input
        ref={inputRef}
        type="file"
        hidden
        accept=".pdf,.doc,.docx,.txt"
        onChange={handleChange}
      />
    </div>
  );
}

export default UploadBox;