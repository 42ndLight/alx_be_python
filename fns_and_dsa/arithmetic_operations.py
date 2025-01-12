def perform_operation(num1, num2, operation):
    """
    Perform an arithmetic operation on two numbers.

    Parameters:
    - num1 (float): The first number.
    - num2 (float): The second number.
    - operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    - float: The result of the arithmetic operation.
    - str: A specific message if the operation is invalid or division by zero occurs.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Division by zero is undefined"
        return num1 / num2
    else:
        return f"Invalid operation: {operation}. Choose from 'add', 'subtract', 'multiply', 'divide'."
