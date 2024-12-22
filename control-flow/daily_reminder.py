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
        reminder = f"Reminder: '{task}' is a HIGH PRIORITY task."
        if time_bound == "yes":
            reminder += " Immediate action is required as it is time-sensitive!"
        else:
            reminder += " Please complete this as soon as possible."

    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM PRIORITY task."
        if time_bound == "yes":
            reminder += " It requires attention today."
        else:
            reminder += " Try to complete it soon."

    case "low":
        reminder = f"Reminder: '{task}' is a LOW PRIORITY task."
        if time_bound == "yes":
            reminder += " Completing it today would be ideal."
        else:
            reminder += " Consider finishing it when you have free time."

# Display the reminder
print(f"\n{reminder}\n")
