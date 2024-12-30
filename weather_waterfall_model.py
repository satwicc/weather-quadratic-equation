def get_user_input():
    """Stage 1: Get user input for T, H, and W."""
    print("Stage 1: Input Weather Parameters")
    while True:
        try:
            T = float(input("Enter temperature (T): "))
            H = float(input("Enter humidity (H): "))
            W = float(input("Enter wind speed (W): "))
            if T < -273.15:
                raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
            if H < 0 or H > 100:
                raise ValueError("Humidity must be between 0 and 100.")
            if W < 0:
                raise ValueError("Windspeed cannot be negative")
            return T, H, W
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid numeric values.")

def calculate_weather_result(T, H, W):
    """Stage 2: Calculate the weather result using the quadratic equation."""
    print("\nStage 2: Calculating Weather Result")
    result = 0.5 * T**2 - 0.2 * H + 0.1 * W - 15
    print(f"Calculated Result: {result}")
    return result

def categorize_weather(result, sunny_threshold=300, stormy_upper=300, stormy_lower=200, rainy_threshold=100):
    """Stage 3: Categorize the weather based on the result."""
    print("\nStage 3: Categorizing Weather")
    if result > sunny_threshold:
        print("The weather is Sunny")
    elif stormy_lower < result <= stormy_upper:
        print("The Weather is Stormy")
    elif result < rainy_threshold:
        print("The weather is Rainy")
    else:
        print("The weather is Cloudy")
    return

def main():
    """Main function to execute the weather model in a waterfall manner."""
    print("Starting Weather Model (Waterfall Model)")

    # Stage 1: Input
    T, H, W = get_user_input()

    # Stage 2: Calculation
    result = calculate_weather_result(T, H, W)

    # Stage 3: Categorization
    categorize_weather(result)

    print("\nWeather Model Complete.")

if __name__ == "__main__":
    main()