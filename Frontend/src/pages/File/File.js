import React, { useState } from "react";

const FileUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [errorMessage, setErrorMessage] = useState("");

  const handleFileChange = (e) => {
    const file = e.target.files[0];

    if (file) {
      if (file.size > 2 * 1024 * 1024) {
        setErrorMessage("File size exceeds 2 MB limit");
      } else {
        setSelectedFile(file);
        setErrorMessage("");
      }
    }
  };

  const handleRemoveFile = () => {
    setSelectedFile(null);
  };

  return (
    <div>
      <input
        className="center-div"
        type="file"
        accept=".pdf, .docx, .doc, .xls, .xlsx"
        onChange={handleFileChange}
      />

      {selectedFile && (
        <div>
          {/* <p className="file-name">Selected File: {selectedFile.name}</p> */}
          <button className="file-preview-btn" onClick={handleRemoveFile}>
            Remove File
          </button>
        </div>
      )}

      {errorMessage && <p className="error-message">{errorMessage}</p>}
    </div>
  );
};

export default FileUpload;
