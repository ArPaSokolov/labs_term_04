<?php
/* Imagine a lot of code here */
$very_bad_unclear_name = "15 chicken wings";


// Write your code here:
/** Assignment reference */
$order = &$very_bad_unclear_name; // new variable as a reference

$order .= " and 1 can of Coke"; // extension string

// Don't change the line below
echo "\nYour order is: $very_bad_unclear_name.";

/** Numbers */
$intVariable = 8;

$floatVariable = 1.5;

$last_month = 1187.23;
$this_month = 1089.98;
$difference = abs($last_month-$this_month);

$message = <<<message
Насколько больше я потратил в прошлом месяце, чем в этом месяце? 
В прошлом месяце я потратил {$last_month}, а в этом месяце я потратил {$this_month}.
Тогда разница между расходами в прошлом месяце и в этом месяце равна {$difference}.
message;

echo "\n$intVariable";
echo "\n";
echo $floatVariable;
echo "\n$intVariable * $floatVariable"; // output = 12
echo "\n$message";
