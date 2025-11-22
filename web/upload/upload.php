<?php

$target_dir = "uploads/";
$file = $_FILES["file"];
$filename = basename($file["name"]);
$target_file = $target_dir . $filename;

// Accept only JPG extension
$ext = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));
if ($ext !== "jpg") {
    die("Only JPG files are allowed.");
}

// No MIME type verification
// No content validation

// File is moved directly
if (move_uploaded_file($file["tmp_name"], $target_file)) {
    echo "Uploaded successfully!<br>";
    echo "<a href='index.php?file={$filename}'>View File</a>";
} else {
    echo "Upload failed.";
}
