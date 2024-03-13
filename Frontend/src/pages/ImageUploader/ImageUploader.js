import React, { useState } from "react";

const ImageUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [previewImage, setPreviewImage] = useState(null);
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    const file = e.target.files[0];

    if (file) {
      // Check file size
      if (file.size > 2 * 1024 * 1024) {
        setError("File size exceeds 2 MB limit");
        return;
      }

      // Set selected file and preview image
      setSelectedFile(file);
      setPreviewImage(URL.createObjectURL(file));
      setError("");
    }
  };

  const handleRemoveImage = () => {
    setSelectedFile(null);
    setPreviewImage(null);
    setError("");
  };

  return (
    <div>
      <input
        className="center-div"
        type="file"
        accept="image/jpeg, image/jpg, image/png"
        onChange={handleFileChange}
      />
      {error && <p className="error-message">{error}</p>}
      {previewImage && (
        <div>
          <img className="image-preview" src={previewImage} alt="Preview" />
          <button className="image-preview-btn" onClick={handleRemoveImage}>
            Remove
          </button>
        </div>
      )}
    </div>
  );
};

export default ImageUpload;
