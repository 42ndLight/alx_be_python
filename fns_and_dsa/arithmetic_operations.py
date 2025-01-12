def perform_operation(num1: float, num2: float, operation: str) -> float:
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if b == 0:
                raise ValueError("Cannot divide by zero!")
            else:
                return num1 / num2
        
