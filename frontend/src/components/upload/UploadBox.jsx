import { useRef } from "react";

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
      className="border-2 border-dashed border-blue-400 rounded-xl p-12 text-center bg-white"
    >
      <h2 className="text-2xl font-bold">
        Upload Your Notes
      </h2>

      <p className="text-gray-500 mt-3">
        PDF, DOCX or TXT
      </p>

      <button
        onClick={handleClick}
        className="mt-8 bg-blue-600 text-white px-8 py-3 rounded-lg"
      >
        Browse Files
      </button>

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