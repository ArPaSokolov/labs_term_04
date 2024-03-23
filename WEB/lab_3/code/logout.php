<?php
session_start();

if (isset($_POST['logout'])) {
    // Уничтожение всех данных сессии
    session_unset();
    session_destroy();
}

// Перенаправление на другую страницу
header('Location: index.php');
exit();
