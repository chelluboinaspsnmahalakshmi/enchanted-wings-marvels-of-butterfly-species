<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>🦋 Enchanted Wings: Marvels of Butterfly Species</title>
</head>
<body>
    <h1>🦋 Enchanted Wings</h1>
    <h2>Butterfly Species Classifier</h2>

    <form action="/predict" method="post" enctype="multipart/form-data">
        <label>Select a Butterfly Image:</label><br><br>
        <input type="file" name="image" accept="image/*" required><br><br>
        <input type="submit" value="Classify">
    </form>

    {% if prediction %}
        <h3>Predicted Species: {{ prediction }}</h3>
        <img src="{{ img_path }}" alt="Butterfly Image" width="300">
    {% endif %}
</body>
</html>
