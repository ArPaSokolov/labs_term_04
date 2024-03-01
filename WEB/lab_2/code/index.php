<?php
/* Imagine a lot of code here */
$very_bad_unclear_name = "15 chicken wings";


// Write your code here:
$order = &$very_bad_unclear_name; // new variable as a reference

$order .= " and 1 can of Coke"; // extension string

// Don't change the line below
echo "\nYour order is: $very_bad_unclear_name.";
