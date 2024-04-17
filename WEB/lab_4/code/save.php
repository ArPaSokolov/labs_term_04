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

    // Указываем диапазон ячеек (в данном случае, первая ячейка A1)
    $range = 'Sheet1!A1';

    // Создаем тело запроса для записи значения "OK"
    $body = new Google\Service\Sheets\ValueRange([
        'values' => [['OK']]
    ]);

    // Устанавливаем параметры записи (здесь можно указать дополнительные настройки)
    $params = [
        'valueInputOption' => 'RAW'
    ];

    // Выполняем запись данных
    $result = $service->spreadsheets_values->update($spreadsheetId, $range, $body, $params);

} catch (Exception $e) {
    echo $e->getMessage() . ' save.php' . $e->getLine() . ' ' . $e->getFile() . ' ' . $e->getCode();
}

// Возвращаемся на страницу с объявлениями
header('Location: board.php');
exit();
?>