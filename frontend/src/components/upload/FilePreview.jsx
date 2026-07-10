function FilePreview({ file, removeFile }) {
  if (!file) return null;

  return (
    <div className="bg-white mt-8 p-6 rounded-xl shadow">

      <h2 className="text-xl font-bold mb-4">
        Selected File
      </h2>

      <p>
        📄 {file.name}
      </p>

      <p className="text-gray-500 mt-2">
        {(file.size / 1024 / 1024).toFixed(2)} MB
      </p>

      <button
        onClick={removeFile}
        className="mt-4 bg-red-600 text-white px-5 py-2 rounded"
      >
        Remove
      </button>

    </div>
  );
}

export default FilePreview;