def perform_operation(a: float, b: float, operator: str) -> float:
    match operator:
        case 'add':
            return a + b
        case 'subtract':
            return a - b
        case 'multiply':
            return a * b
        case 'divide':
            if b == 0:
                raise ValueError("Cannot divide by zero!")
            else:
                return a / b
        
print(perform_operation(5, 3, 'add'))  # Output: 8