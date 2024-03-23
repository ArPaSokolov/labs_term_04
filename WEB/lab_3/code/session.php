<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Получение данных из формы
    $surname = $_POST['surname'];
    $name = $_POST['name'];
    $age = $_POST['age'];

    // Сохранение данных в сессию
    $_SESSION['surname'] = $surname;
    $_SESSION['name'] = $name;
    $_SESSION['age'] = $age;

    // Перенаправление на другую страницу
    header("Location: index.php");
    exit();
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Session</title>
    <style>
        body {
            height: 100vh;
            width: 30vh;
        }

        input {
            width: 100%;
            padding: 5px;
            margin-bottom: 10px;
        }

    </style>
</head>
<body>
<form method="post" action="<?php echo $_SERVER['PHP_SELF']?>">
    <h1>Session</h1>
    <h2>Task 2</h2>

    <label>Surname:</label>
    <input type="text" name="surname" required><br>

    <label>Name:</label>
    <input type="text" name="name" required><br>

    <label>Age:</label>
    <input type="number" name="age" required><br>

    <button type="submit">Save profile</button>
</form>

<form action="logout.php" method="post">
    <button type="submit" name="logout">Exit profile</button>
</form>

<a href="index.php"><h2>Back</h2></a>
</body>
</html>
