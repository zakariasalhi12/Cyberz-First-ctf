<!DOCTYPE html>
<html>
<head>
    <title>Upload your image</title>
</head>
<body>
    <h2>Upload Profile Image</h2>

    <form action="upload.php" method="POST" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>

    <?php
    if (isset($_GET['file'])) {
        echo "<h3>Uploaded Image:</h3>";
        echo "<img src='uploads/" . htmlspecialchars($_GET['file']) . "' width='200'>";
    }
    ?>
</body>
</html>
