<!DOCTYPE html>
<html>
<head>
    <title>Party Planner Form</title>
</head>
<body>
    <h1>Party Planner</h1>

    <?php
    // Get and display the public IP address
    $publicIP = trim(shell_exec('curl -4 ifconfig.io 2>/dev/null'));
    if (!empty($publicIP)) {
        echo "<p><strong>Public IP Address:</strong> " . htmlspecialchars($publicIP) . "</p>";
    } else {
        echo "<p><strong>Could not retrieve public IP address.</strong></p>";
    }

    $items = [
        "Cake", "Balloons", "Music System", "Lights", "Catering Service",
        "DJ", "Photo Booth", "Tables", "Chairs", "Drinks",
        "Party Hats", "Streamers", "Invitation Cards", "Party Games", "Cleaning Service"
    ];
    ?>

    <form action="process.php" method="post">
        <p>Select party items:</p>
        <?php
        foreach ($items as $index => $item) {
            echo "<label><input type='checkbox' name='items[]' value='$index'> $item</label><br>";
        }
        ?>
        <br>
        <input type="submit" value="Plan Party">
    </form>
</body>
</html>
