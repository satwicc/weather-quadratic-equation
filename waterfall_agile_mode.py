import random

def get_user_input():
    print("Sprint 1: Basic User Input")
    while True:
        try:
            T = float(input("Enter temperature (T): "))
            return T
        except ValueError:
            print("Invalid input. Please enter a valid number for temperature.")

def calculate_weather_result(T):
    print("\nSprint 2: Basic Calculation")
    result = 0.5 * T**2 - 15
    print(f"Calculated Result (using only T): {result}")
    return result

def categorize_weather(result):
    print("\nSprint 3: Basic Categorization")
    if result > 300:
        print("The weather is Sunny")
    elif result > 0:
        print("The Weather is Unstable")
    else:
        print("The weather is Calm")
    return

def add_humidity(T):
    print("\nSprint 4: Adding Humidity")
    while True:
        try:
            H = float(input("Enter humidity (H): "))
            if H < 0 or H > 100:
                raise ValueError("Humidity must be between 0 and 100.")
            break
        except ValueError:
            print("Invalid input for humidity. Please enter a number between 0 and 100")
    result = 0.5 * T**2 - 0.2 * H - 15
    print(f"Calculated Result (with H): {result}")
    return result

def add_wind(T, H):
    print("\nSprint 5: Adding Wind and Refining Categories")
    while True:
        try:
            W = float(input("Enter wind speed (W): "))
            if W < 0:
                raise ValueError("Windspeed cannot be negative")
            break
        except ValueError:
            print("Invalid input for Windspeed. Please enter a non-negative number")
    result = 0.5 * T**2 - 0.2 * H + 0.1*W - 15
    print(f"Calculated Result (with H and W): {result}")
    if result > 300:
        print("The weather is Sunny")
    elif 200 < result <= 300:
        print("The Weather is Stormy")
    elif result < 100:
        print("The weather is Rainy")
    else:
        print("The weather is Cloudy")
    return

def main_agile():
    print("Starting Weather Model (Agile Model)")

    T = get_user_input()
    result = calculate_weather_result(T)
    categorize_weather(result)
    result = add_humidity(T)
    add_wind(T, result)

    print("\nWeather Model Development Complete (Agile).")

if __name__ == "__main__":
    main_agile()