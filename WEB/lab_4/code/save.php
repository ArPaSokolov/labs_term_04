<?php
require __DIR__ . '/vendor/autoload.php'; // Подключаем Google API Client Library

try {
    // Конфигурируем Google Client
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

    // Получаем данные с доски объявлений
    if ($_SERVER["REQUEST_METHOD"] === "POST") {
        $email = $_POST["email"] ?? '';
        $categories = $_POST["categories"] ?? '';
        $title = $_POST["title"] ?? '';
        $description = $_POST['text'] ?? '';

        // Данные для записи
        $values = [
            [$email, $categories, $title, $description]
        ];
    }

    // Записываем данные в таблицу
    $body = new Google_Service_Sheets_ValueRange([
        'values' => $values
    ]);
    $params = [
        'valueInputOption' => 'RAW'
    ];

    // Выполняем запись данных
    $result = $service->spreadsheets_values->append($spreadsheetId, $range, $body, $params);

} catch (Exception $e) {
    echo $e->getMessage() . ' save.php' . $e->getLine() . ' ' . $e->getFile() . ' ' . $e->getCode();
}

// Взврат на страницу с объявлениями
header('Location: board.php');
exit();
?>