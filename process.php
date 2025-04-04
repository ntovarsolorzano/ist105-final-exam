<?php
if (!isset($_POST['items'])) {
    echo "<p>No items selected. Please go back and choose at least one.</p>";
    exit;
}

$selected = $_POST['items'];
$arg_string = implode(",", array_map('intval', $selected)); // Ensures only numbers

$escaped_arg = escapeshellarg($arg_string);
$output = shell_exec("python3 party_planner.py $escaped_arg 2>&1");

echo $output;
?>
