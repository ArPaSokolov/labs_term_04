<?php
/* Подключение к серверу MySQL */
$mysqli = new mysqli('db', 'root', 'helloworld', 'web', "6603");

if (!$mysqli->query('INSERT INTO ad (email, title, description, category) VALUES("test@test.com", "title", "desc", "other")')) {
    printf("Ошибка при выполнении запроса: %s\n", $mysqli->error);
}
?>

<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>lab_4</title>
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
