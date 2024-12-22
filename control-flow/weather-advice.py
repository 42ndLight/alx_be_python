#!/usr/bin/python3

def get_weather_advice():
    """
    Ask user for weather conditions and provide clothing recommendations.
    """
    # Get weather input from user
    weather = input("What's the weather like today? (sunny/rainy/cold): ")

    # Provide recommendations based on weather conditions
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

if __name__ == "__main__":
    get_weather_advice()