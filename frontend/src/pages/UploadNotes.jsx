import { useState } from "react";

import DashboardLayout from "../layouts/DashboardLayout";

import UploadBox from "../components/upload/UploadBox";
import FilePreview from "../components/upload/FilePreview";
import UploadProgress from "../components/upload/UploadProgress";

function UploadNotes() {
  const [file, setFile] = useState(null);
  const [progress, setProgress] = useState(0);

  const uploadFile = () => {
    if (!file) {
      alert("Please choose a file");
      return;
    }

    setProgress(0);

    let value = 0;

    const timer = setInterval(() => {
      value += 10;

      setProgress(value);

      if (value >= 100) {
        clearInterval(timer);
      }
    }, 200);
  };

  return (
    <DashboardLayout>

      <div className="max-w-6xl mx-auto">

        <div className="mb-10">

          <h1 className="text-4xl font-bold text-slate-800">
            Upload Study Notes
          </h1>

          <p className="text-gray-500 mt-3">
            Upload your notes and let AI generate summaries,
            quizzes and important questions automatically.
          </p>

        </div>

        <UploadBox onFileSelect={setFile} />

        <FilePreview
          file={file}
          removeFile={() => {
            setFile(null);
            setProgress(0);
          }}
        />

        {file && (
          <>
            <button
              onClick={uploadFile}
              className="
              mt-8
              bg-gradient-to-r
              from-green-500
              to-emerald-600
              hover:scale-105
              transition
              text-white
              px-8
              py-3
              rounded-xl
              font-semibold
              "
            >
              Upload Notes
            </button>

            <UploadProgress progress={progress} />
          </>
        )}

        <div
          className="
          mt-10
          bg-blue-50
          rounded-3xl
          p-8
          border
          border-blue-200
          "
        >
          <h2 className="text-2xl font-bold mb-4">
            💡 AI Tips
          </h2>

          <ul className="space-y-3 text-gray-700">

            <li>✅ Maximum file size: 20 MB</li>

            <li>✅ Supported formats: PDF, DOC, DOCX, TXT</li>

            <li>✅ AI automatically extracts text</li>

            <li>✅ Generate quizzes in one click</li>

            <li>✅ View upload history later</li>

          </ul>

        </div>

      </div>

    </DashboardLayout>
  );
}

export default UploadNotes;