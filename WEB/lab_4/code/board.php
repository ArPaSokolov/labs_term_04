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

<form action="save.php" method="POST">
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
            require __DIR__ . '/vendor/autoload.php'; // Подключаем Google API Client Library

            $client = new \Google_Client();
            $client->setApplicationName('The Bulletin Board');
            $client->setScopes(['https://www.googleapis.com/auth/spreadsheets']);
            $client->setAccessType('offline');
            $path = __DIR__ . '/credentials.json';
            $client->setAuthConfig($path);

            // Конфигурируем Sheets Service
            $service = new Google\Service\Sheets($client);

            // Идентификатор таблицы
            $spreadsheetId = '1jnexgBDAHJq3gzLwzfbyHRkSLQa2EyOMPogOjvwYk9M';

            // Определение диапазона для записи
            $range = 'Sheet1!A:D';

            $service = new Google_Service_Sheets($client);
            $response = $service->spreadsheets_values->get($spreadsheetId, $range);
            $values = $response->getValues();

            // Отображение данных в виде таблицы
            if (!empty($values)) {
                $isFirstRow = true; // Флаг для определения первой строки
                foreach ($values as $row) {
                    if ($isFirstRow) {
                        $isFirstRow = false;
                        continue; // Пропускаем первую строку
                    }
                    echo '<tr>';
                    foreach ($row as $cell) {
                        echo '<td>' . htmlspecialchars($cell) . '</td>';
                    }
                    echo '</tr>';
                }
            } else {
                echo 'No data available.';
            }
            ?>
        </tbody>
    </table>
</div>
</body>
</html>