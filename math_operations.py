#!/usr/bin/env python3
import sys
import requests

def perform_operation(num1, num2, operation):
    try:
        if operation == "add":
            result = num1 + num2
            op_symbol = "+"
        elif operation == "sub":
            result = num1 - num2
            op_symbol = "-"
        elif operation == "mul":
            result = num1 * num2
            op_symbol = "×"
        elif operation == "div":
            if num2 == 0:
                html = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>Error</title>
                    </head>
                    <body>
                        <h2>Error:Cannot be divided by zero.</h2>
                        <a href="math_form.php">Back to Top</a>
                    </body>
                    </html>
                    """
                print(html)
                sys.exit(1)
            result = num1 / num2
            op_symbol = "÷"
        if result > 100:
            result = result * 2
        elif result < 0:
            result = result + 50
        return {
            "result": result,
            "operation": op_symbol,
        }
    except ValueError:
        return {"error": "Invalid number input!"}
    except Exception as e:
        return {"error": str(e)}

def get_ec2_public_ip():
    try:
        response = requests.get('http://169.254.169.254/latest/meta-data/public-ipv4', timeout=2)
        return response.text
    except:
        return "Could not retrieve public IP"

if __name__ == "__main__":
    input1 = int(sys.argv[1])
    input2 = int(sys.argv[2])
    operation = sys.argv[3]
    host = sys.argv[4]
    ec2_host = get_ec2_public_ip()

    result = perform_operation(input1, input2, operation)

    if "error" in result:
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Error</title>
        </head>
        <body>
            <h2>Error:</h2>
            <p>{result['error']}</p>
            <a href="math_form.php">Back to Top</a>
        </body>
        </html>
        """
    else:
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Calculation Result</title>
        </head>
        <body>
            <h2>Result:</h2>
            <p>Operation: {result['operation']} </p>
            <p>Input1: {input1}</p> 
            <p>Input2: {input2}</p>
            <p>Result: {result['result']}</p>
            <a href="math_form.php">Back to Top</a>
            <p>This result was processed on my EC2 instance with Public IP: {ec2_host}</p>
            <p>Access the application via Load Balancer URL: {host}</p>
        </body>
        </html>
        """
    
        print(html)