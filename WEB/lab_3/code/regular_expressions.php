<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Regular expressions</title>
</head>
<body>
    <h1>Regular expressions</h1>
    <h2>Task 1</h2>
    <?php
    $pattern = '/a..b/'; // регулярка
    $text = 'ahb acb aeb aeeb bdha aj ab adcb axeb acctb';

    preg_match_all($pattern, $text, $matches);
    echo "Строки подошедшие под шаблон:<br>";
    foreach ($matches[0] as $match) {
        echo $match."<br>";
    }
    ?>

    <h2>Task 2</h2>
    <?php
    // Task 2
    function cubing($matches): string // возводим в куб
    {
        return $matches[0] ** 3;
    }

    $pattern = '/(\d+)/'; // регулярка
    $string = 'a1b2c3d4e5';

    $stringWithCubes = preg_replace_callback($pattern, 'cubing', $string);

    echo "Новая строка с кубами:<br>" . $stringWithCubes . "<br>";
    ?>

    <a href="index.php"><h2>Back</h2></a>
</body>
</html>
