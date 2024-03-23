<title>Form</title>
<h1>Form</h1>
<h2>Task 1</h2>

<?php
if ('POST' === $_SERVER['REQUEST_METHOD']) {
    if (isset($_POST['text'])) {
        $text = $_POST['text'];

        // подсчет количества слов и символов
        $wordCount = 0;
        if (!empty($text)) {
            $words = preg_split('/\s+/', $text);
            $wordCount = count($words);
        }
        $charCount = mb_strlen($text, "utf-8");

        // вывод результатов
        echo "Количество слов: $wordCount<br>";
        echo "Количество символов: $charCount";
    }
}
?>

<form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
    <label>
        <textarea name="text" rows="3" cols="50"><?php echo htmlspecialchars($text ?? ''); ?></textarea>
    </label><br>
    <button type="submit">Подсчитать</button>
</form>

<a href="index.php"><h2>Back</h2></a>
