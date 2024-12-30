def weather_model_file_single(weather_file1):
    print("\nWeather Modeling (File Input - Single Set)")
    try:
        with open(weather_file1, "r") as file:  # Open in "r" (read) mode
            line = file.readline().strip()
            if not line:
                print("Error: Input file is empty.")
                return

            values = line.split(',')
            if len(values) != 3:
                print("Error: Incorrect number of values in input file. Expected 3 (T, H, W).")
                return
            try:
                T = float(values[0])
                H = float(values[1])
                W = float(values[2])
            except ValueError:
                print("Error: Non-numeric data in the input file")
                return

            result = 0.5 * T**2 - 0.2 * H + 0.1 * W - 15
            print(f"Result: {result}")

    except FileNotFoundError:
        print(f"Error: File '{weather_file1}' not found.") # Corrected variable name here as well
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#Example Usage (Important: Create the input file FIRST)
with open("input_single.txt", "w") as f:
    f.write("25,60,10")

weather_model_file_single("input_single.txt")