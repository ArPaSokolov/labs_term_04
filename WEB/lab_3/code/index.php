<?php
session_start();

// Получение сохраненных данных из сессии
$surname = $_SESSION['surname'] ?? '';
$name = $_SESSION['name'] ?? 'Unknown';
$age = $_SESSION['age'] ?? '';
?>

<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>lab_3</title>
</head>
<body>
    <p><?php echo "$surname $name $age"; ?></p>

    <h1>Сontents:</h1>

    <a href="regular_expressions.php"><h2>Regular expressions</h2></a>

    <a href="form.php"><h2>Form</h2></a>

    <a href="session.php"><h2>Session</h2></a>
</body>
</html>
