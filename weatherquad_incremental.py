# Incremental model
def calculate_weather_model(T, H, W):
    return 0.5 * T**2 - 0.2 * H + 0.1 * W - 15

def categorize_weather(weather_value):
    if weather_value >= 20:
        return "Sunny"
    elif 10 <= weather_value < 20:
        return "Cloudy"
    elif 0 <= weather_value < 10:
        return "Rainy"
    else:
        return "Stormy"

def increment_1():
    T, H, W = 30, 50, 10
    weather_value = calculate_weather_model(T, H, W)
    category = categorize_weather(weather_value)
    print(f"Increment 1: W = {weather_value:.2f}, Category = {category}")

def increment_2():
    try:
        T = float(input("Enter Temperature (T): "))
        H = float(input("Enter Humidity (H): "))
        W = float(input("Enter Wind Speed (W): "))
        weather_value = calculate_weather_model(T, H, W)
        category = categorize_weather(weather_value)
        print(f"Increment 2: W = {weather_value:.2f}, Category = {category}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

def increment_3():
    try:
        with open("spam.txt", "r") as file:
            line = file.readline().strip()
            T, H, W = map(float, line.split())
            weather_value = calculate_weather_model(T, H, W)
            category = categorize_weather(weather_value)
            print(f"Increment 3: W = {weather_value:.2f}, Category = {category}")
    except FileNotFoundError:
        print("Error: File 'spam.txt' not found.")
    except ValueError:
        print("Error: Invalid data format in 'spam.txt'.")

def increment_4():
    try:
        with open("spam.txt", "r") as file:
            lines = file.readlines()
        for idx, line in enumerate(lines):
            try:
                T, H, W = map(float, line.strip().split())
                weather_value = calculate_weather_model(T, H, W)
                category = categorize_weather(weather_value)
                print(f"Increment 4 (Set {idx + 1}): W = {weather_value:.2f}, Category = {category}")
            except ValueError:
                print(f"Error: Invalid data format on line {idx + 1}. Skipping.")
    except FileNotFoundError:
        print("Error: File 'spam.txt' not found.")

def increment_5():
    try:
        num_sets = int(input("Enter the number of input sets: "))
        for i in range(num_sets):
            print(f"\nSet {i + 1}:")
            T = float(input("Enter Temperature (T): "))
            H = float(input("Enter Humidity (H): "))
            W = float(input("Enter Wind Speed (W): "))
            weather_value = calculate_weather_model(T, H, W)
            category = categorize_weather(weather_value)
            print(f"Increment 5 (Set {i + 1}): W = {weather_value:.2f}, Category = {category}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

def main():
    print("Incremental Model for Weather Prediction")
    print("1. Increment 1: Hardcoded Values")
    print("2. Increment 2: Keyboard Input")
    print("3. Increment 3: File Input (Single Set)")
    print("4. Increment 4: File Input (Multiple Sets)")
    print("5. Increment 5: Loop for Multiple Keyboard Inputs")
    
    try:
        choice = int(input("Choose an increment (1-5): "))
        if choice == 1:
            increment_1()
        elif choice == 2:
            increment_2()
        elif choice == 3:
            increment_3()
        elif choice == 4:
            increment_4()
        elif choice == 5:
            increment_5()
        else:
            print("Invalid choice. Exiting.")
    except ValueError:
        print("Error: Please enter a valid numeric choice.")

if __name__ == "__main__":
    main()
