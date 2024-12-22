#!/usr/bin/python3
"""
A script that creates customized reminders for a single daily task
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
if time_bound == "yes":
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task that requires attention today."
        case "low":
            reminder = f"Reminder: '{task}' is a low priority task. Please complete it today if possible."
else:
    match priority:
        case "high":
            reminder = f"Note: '{task}' is a high priority task. Please complete this as soon as possible."
        case "medium":
            reminder = f"Note: '{task}' is a medium priority task. Try to complete it soon."
        case "low":
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

# Display the reminder
print(f"\n{reminder}\n")
