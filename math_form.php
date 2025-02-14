<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Input Form</title>
</head>
<body>
    <h2>Welcome to the Mathematical Application!</h2>
    <h2>This application is hosted on my EC2 instance with Public IP: <?php //echo file_get_contents('http://169.254.169.254/latest/meta-data/public-ipv4'); ?></h2>
         <h2>Enter two numbers and select an operation to calculate the result.</h2>
    <form action="process_math.php" method="POST">
        <div>
            <label for="input1">Number 1:</label>
            <input type="number" id="input1" name="input1" required/>
        </div>
        <div>
            <label for="input2">Number 2:</label>
            <input type="number" id="input2" name="input2" required/>
        </div>
        <div>
        <label for="operation">Operation:</label>
            <select id="operation" name="operation" required>
                <option value="add">Addition</option>
                <option value="sub">Subtraction</option>
                <option value="mul">Multiplication</option>
                <option value="div">Division</option>
            </select>
        </div>
        <button type="submit">Calculate</button>
    </form>
</body>
</html>