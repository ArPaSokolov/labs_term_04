<?php
// Подключение к серверу MySQL
$mysqli = new mysqli('db', 'root', 'helloworld', 'web');

if (mysqli_connect_errno()) {
    printf("Подключение к серверу MySQL невозможно. Код ошибки: %s\n", mysqli_connect_error());
    exit;
}

// Обработка формы
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = $mysqli->real_escape_string($_POST['email']);
    $title = $mysqli->real_escape_string($_POST['title']);
    $category = $mysqli->real_escape_string($_POST['categories']);
    $description = $mysqli->real_escape_string($_POST['text']);

    $query = "INSERT INTO ad (email, title, description, category) VALUES ('$email', '$title', '$description', '$category')";
    $mysqli->query($query);
}

// Получение всех объявлений
$ads = [];
if ($result = $mysqli->query('SELECT * FROM ad ORDER BY created DESC')) {
    while ($row = $result->fetch_assoc()) {
        $ads[] = $row;
    }
    $result->close();
}

// Закрытие соединения
$mysqli->close();
?>

<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>lab_5</title>
</head>
<body>
<h1>The Bulletin Board</h1>

<form action="board.php" method="POST">
    <label for="email">Email</label>
    <input type="email" name="email" required><br>

    <label for="title">Title</label>
    <input type="text" name="title" required><br>

    <label for="categories">Categories</label>
    <select name="categories" required>
        <option value="clothes">Clothes</option>
        <option value="electronics">Electronics</option>
        <option value="services">Services</option>
    </select><br>

    <label for="description">Description:</label><br>
    <textarea name="text" rows="10" cols="54" required></textarea><br>

    <button type="submit">Post</button>
</form>
</form>
<div id="table">
    <table>
        <thead>
        <tr>
            <th>Email</th>
            <th>Title</th>
            <th>Description</th>
            <th>Category</th>
        </tr>
        </thead>
        <tbody>
        <?php foreach ($ads as $ad):
            echo "<tr>";
                echo "<td>" . ($ad['email']) . "</td>";
                echo "<td>" . ($ad['title']) . "</td>";
                echo "<td>" . ($ad['description']) . "</td>";
                echo "<td>" . ($ad['category']) . "</td>";
            echo "</tr>";
        endforeach; ?>
        </tbody>
    </table>
</div>
</body>
</html>