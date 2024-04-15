<?php
require_once __DIR__ . '/vendor/autoload.php'; // Подключаем Google API Client Library

use Google\Spreadsheet\DefaultServiceRequest;
use Google\Spreadsheet\ServiceRequestFactory;

putenv('GOOGLE_APPLICATION_CREDENTIALS=' . __DIR__ . '/credentials.json');
$client = new Google_Client();

try {
    $client->useApplicationDefaultCredentials();
    $client->setApplicationName('The Bulletin Board');

    $accessToken = $client->fetchAccessTokenWithAssertion()["access_token"];
    ServiceRequestFactory::setInstance(new DefaultServiceRequest($accessToken));

    // Получаем нашу таблицу
    $spreadsheet = (new Google\Spreadsheet\SpreadsheetService)
        ->getSpreadsheetFeed()
        ->getByTitle('The Bulletin Board');

    // Получаем первый лист (вкладку)
    $worksheets = $spreadsheet->getWorksheetFeed()->getEntries();
    $worksheet = $worksheets[0];

    // Вписываем значение "OK" в первую ячейку
    $cellFeed = $worksheet->getCellFeed();
    $cellFeed->editCell(1, 1, 'OK');

} catch (Exception $e) {
    echo $e->getMessage() . ' save.php' . $e->getLine() . ' ' . $e->getFile() . ' ' . $e->getCode();
}

// возвращает на страницу с объявлениями
header('Location: board.php');
exit();
