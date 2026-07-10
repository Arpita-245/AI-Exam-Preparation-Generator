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
            className="mt-8 bg-green-600 text-white px-8 py-3 rounded-lg"
          >
            Upload
          </button>

          <UploadProgress progress={progress} />
        </>
      )}

    </DashboardLayout>

  );
}

export default UploadNotes;