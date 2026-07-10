function UploadProgress({ progress }) {

  return (

    <div className="bg-white mt-8 p-6 rounded-xl shadow">

      <h2 className="font-bold mb-4">
        Upload Progress
      </h2>

      <div className="w-full bg-gray-200 rounded-full h-4">

        <div
          className="bg-blue-600 h-4 rounded-full"
          style={{ width: `${progress}%` }}
        ></div>

      </div>

      <p className="mt-3">
        {progress}%
      </p>

    </div>

  );
}

export default UploadProgress;