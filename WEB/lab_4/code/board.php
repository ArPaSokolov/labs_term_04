<?php //require __DIR__ . '/../vendor/autoload.php'; ?>

<doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>lab_3</title>
</head>
<body>
    <h1>The Bulletin Board</h1>

    <form action="save.php" method="post">
        <label for="email">Email</label>
        <input type="email" name="email" required>

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
    <div id="table">
        <table>
            <thead>
            <tr>
                <th>Email</th>
                <th>Title</th>
                <th>Category</th>
                <th>Description</th>
            </tr>
            </thead>
            <tbody>
            <?php
            $categories = ["clothes", "electronics", "services"];
            foreach ($categories as $category) {
                $dir = "/code/categories/$category"; // путь к директории с файлами
                $fileNames = scandir($dir, SCANDIR_SORT_ASCENDING); // получение списка файлов в директории
                foreach ($fileNames as $fileName) {
                    if ($fileName !== '.' && $fileName !== '..') {
                        echo '<tr>';
                        $filePath = $dir . "/" . $fileName; // полный путь к файлу

                        $file = fopen($filePath, "r"); // открыть файл для чтения данных
                        if ($file) {
                            $fileData = file($filePath);

                            foreach ($fileData as $data) {
                                // разделить строку на отдельные значения
                                $values = explode(":", $data);
                                echo "<td>" . $values[1] . "</td>";
                            }
                            fclose($file); // закрыть файл
                        }
                        echo '</tr>';
                    }
                }
            }
            ?>
            </tbody>
        </table>
    </div>
</body>
</html>