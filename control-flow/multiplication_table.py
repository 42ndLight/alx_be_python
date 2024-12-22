#!/usr/bin/python3

# Get input from user
user_input = input("Enter a number to see its multiplication table: ")

try:
    # Convert input to integer
    number = int(user_input)

    # Generate and print multiplication table using for loop
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

except ValueError:
    print("Please enter a valid number.")