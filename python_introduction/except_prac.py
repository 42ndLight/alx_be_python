def divide(x,y):
    if y == 0:
        raise ZeroDivisionError("division by zero")
    return x / y

va1 = float(input("Enter a number: "))
va2 = float(input("Enter another number: "))
print(divide(va1, va2))

pass 

try:
    file1 = open("abc.txt", "r")
    print(file1.read())
except FileNotFoundError:
    print("File not found")

   
class ValueTooHighError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"ValueTooHighError: {self.value} is too high."
    

number = int(input("Enter a number: "))

if number > 100:
    raise ValueTooHighError(number)
else:
    print("The number is:",number)