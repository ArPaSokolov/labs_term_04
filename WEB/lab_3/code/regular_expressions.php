<title>Regular expressions</title>
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
