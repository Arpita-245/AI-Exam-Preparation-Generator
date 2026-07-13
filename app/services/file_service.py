import os
import uuid

from flask import current_app
from werkzeug.utils import secure_filename


def save_uploaded_file(file):
    """
    Save an uploaded file to the uploads folder.

    Returns:
        filename   -> unique filename stored on disk
        file_path  -> filename stored in database
    """

    if file is None:
        raise ValueError("No file provided.")

    # ==========================================
    # Clean original filename
    # ==========================================
    original_filename = secure_filename(file.filename)

    if original_filename == "":
        raise ValueError("Invalid filename.")

    # ==========================================
    # Generate unique filename
    # Example:
    # a1b2c3d4_Data_Structure_Unit_1.pdf
    # ==========================================
    unique_filename = (
        f"{uuid.uuid4().hex[:8]}_{original_filename}"
    )

    # ==========================================
    # Upload folder
    # ==========================================
    upload_folder = current_app.config["UPLOAD_FOLDER"]

    os.makedirs(upload_folder, exist_ok=True)

    # ==========================================
    # Full destination path
    # ==========================================
    full_path = os.path.join(
        upload_folder,
        unique_filename
    )

    # ==========================================
    # Save file
    # ==========================================
    file.save(full_path)

    # Verify file saved successfully
    if not os.path.exists(full_path):
        raise FileNotFoundError(
            "File could not be saved."
        )

    # ==========================================
    # Debug Logs
    # ==========================================
    print("\n" + "=" * 65)
    print("FILE SAVED SUCCESSFULLY")
    print("=" * 65)
    print("Original Filename :", original_filename)
    print("Stored Filename   :", unique_filename)
    print("Upload Folder     :", upload_folder)
    print("Full Path         :", full_path)
    print("File Size         :", os.path.getsize(full_path), "bytes")
    print("=" * 65 + "\n")

    # Store only filename in database
    return unique_filename, unique_filename