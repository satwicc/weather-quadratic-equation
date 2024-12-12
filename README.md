# Weather Report
This project calculates and classifies weather conditions based on three variables: temperature, humidity, and wind speed. The program evaluates the weather using a predefined formula and classifies it into one of three weather types:
- Sunny
- Rainy
- Stormy

## How It Works
The program uses the following equation to calculate a weather value: weather = (0.5 * t^2) - (0.2 * h) + (0.1 * w) - 15

### Where:
t is the temperature (in °C).
h is the humidity (in percentage).
w is the wind speed (in meters per second).

## Weather Classification
The calculated weather value determines the classification:
Sunny: Weather value > 300

Rainy: 200 < Weather value <= 300

Stormy: Weather value < 200

## Features
- Takes user input for temperature, humidity, and wind speed.
- Classifies weather based on simple thresholds.
- User-friendly interface with clear prompts and outputs.

## Requirements
- Python 3.x
