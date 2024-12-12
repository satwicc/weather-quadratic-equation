print ("Enter the following variables to find rthe weather: \n")
temperature = int(input("Enter the Temperture in Celcius: "))
humidity = int(input("Enter the Humidity %: "))
wind = int(input("Enter the Speed of the Wind in m/s: "))
weather = (0.5 * temperature * temperature) - (0.2 * humidity) + (0.1 * wind)- 15
if weather > 300:
    print ("The weather is Sunny")
elif 200 < weather <= 300:
    print ("The Weather is Stormy")
elif (weather < 100):
    print ("The weather is Stormy")
else:
    print ("enter valid things")

print (weather)
