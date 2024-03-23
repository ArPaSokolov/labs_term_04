<?php
// проверка, была ли отправлена форма
if ('POST' === $_SERVER['REQUEST_METHOD']) {
    // получение данных из формы
    $email = $_POST['email'] ?? '';
    $title = $_POST['title'] ?? '';
    $category = $_POST['categories'] ?? '';
    $description = $_POST['text'] ?? '';

    // проверка наличия всех полей
    if (!empty($email) && !empty($title) && !empty($category) && !empty($description)) {
        $fileName = "/code/categories/$category/{$title}_announcements.txt";
        $data = "Email: $email\nTitle: $title\nCategory: $category\nDescription: $description\n";

        $f = fopen($fileName, "w"); // открываем файл, в случае отсутствия - создаем
        fwrite($f, $data); // запись в файл
        fclose($f); // закрываем файл
    }
}

// возвращает на страницу с объявлениями
header('Location: files.php');
exit();
?>