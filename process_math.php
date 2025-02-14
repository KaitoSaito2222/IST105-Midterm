<?php
    $input1 = escapeShellarg($_POST["input1"]);
    $input2 = escapeShellarg($_POST["input2"]);
    $operation = escapeShellarg($_POST["operation"]);
    $host = escapeShellarg($_SERVER['HTTP_HOST']); 
    
    $command = escapeshellcmd("python3 math_operations.py $input1 $input2 $operation $host");
    $output = shell_exec($command);
    if ($output) {
        echo $output;
    } else {
        echo "Error executing Python script";
    }
?>