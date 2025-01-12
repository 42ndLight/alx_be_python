#!/usr/bin/env python3

"""
Temperature conversion tool that demonstrates variable scope using global conversion factors
"""

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FREEZING_POINT_ADJUSTMENT = 32

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit temperature to Celsius using global conversion factor
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    Returns:
        float: Temperature in Celsius
    """
    try:
        fahrenheit = float(fahrenheit)
        return (fahrenheit - FREEZING_POINT_ADJUSTMENT) * FAHRENHEIT_TO_CELSIUS_FACTOR
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit using global conversion factor
    Args:
        celsius (float): Temperature in Celsius
    Returns:
        float: Temperature in Fahrenheit
    """
    try:
        celsius = float(celsius)
        return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_ADJUSTMENT
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def main():
    """Main program loop"""
    while True:
        try:
            # Get temperature input from user
            temp = input("Enter the temperature to convert: ")
            
            # Get temperature unit from user
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
            
            # Validate unit input
            if unit not in ['C', 'F']:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
                continue
            
            # Perform conversion based on input unit
            if unit == 'C':
                result = convert_to_fahrenheit(temp)
                print(f"{float(temp)}°C is {result}°F")
            else:
                result = convert_to_celsius(temp)
                print(f"{float(temp)}°F is {result}°C")
                
            break
            
        except ValueError as e:
            print(e)
            continue

if __name__ == "__main__":
    main()