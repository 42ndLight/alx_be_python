#!/usr/bin/python3
"""
A simplified script that creates customized reminders for a single daily task
based on priority and time sensitivity.
"""

# Get task details from user
task = input("Enter your task: ")

# Get and validate priority
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ['high', 'medium', 'low']:
        break
    print("Invalid priority! Please enter 'high', 'medium', or 'low'")

# Get and validate time sensitivity
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ['yes', 'no']:
        break
    print("Invalid input! Please enter 'yes' or 'no'")

# Create reminder using match-case and if statements
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Please complete this as soon as possible."

    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that requires attention today!"
        else:
            reminder += ". Try to complete this soon."

    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            reminder += ". Please complete it today if possible."
        else:
            reminder += ". Consider completing it when you have free time."

# Display the reminder
print(f"\n{reminder}\n")