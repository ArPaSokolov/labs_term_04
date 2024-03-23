<?php
session_start();

$userData = $_SESSION['userdata'] ?? [];

if ('POST' === $_SERVER['REQUEST_METHOD']) {
    // получение данных из формы
    // Task 2
    $surname = ($_POST['surname'] ?? '');
    $name = ($_POST['name'] ?? '');
    $age = ($_POST['age'] ?? '');
    // Task 3
    $sex = ($_POST['sex'] ?? '');
    $salary = ($_POST['salary'] ?? '');

    // создание массива данных
    // Task 3
    $userData = [
        'surname' => $surname,
        'name' => $name,
        'age' => $age,
        'salary' => $salary,
        'sex' => $sex
    ];

    // сохранение данных в сессию
    $_SESSION['userdata'] = $userData; // массив данных

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
    <h1>Session</h1>

    <form method="post" action="<?php echo $_SERVER['PHP_SELF']?>">
        <h2>Task 2</h2>

        <label>Surname:</label>
        <input type="text" name="surname" value="<?php echo $userData['surname'] ?? '*'; ?>" required><br>

        <label>Name:</label>
        <input type="text" name="name" value="<?php echo $userData['name'] ?? '*'; ?>" required><br>

        <label>Age:</label>
        <input type="text" name="age" value="<?php echo $userData['age'] ?? '*'; ?>" required><br>

    <h2>Task 3</h2>

        <label>Sex:</label>
        <input type="text" name="sex" value="<?php echo $userData['sex'] ?? ''; ?>"><br>

        <label>Salary:</label>
        <input type="text" name="salary" value="<?php echo $userData['salary'] ?? ''; ?>"><br>

        <button type="submit">Save</button>
    </form><br>

    <form action="logout.php" method="post">
        <button type="submit" name="logout">Delete profile</button>
    </form>

    <a href="index.php"><h2>Back</h2></a>
</body>
</html>
