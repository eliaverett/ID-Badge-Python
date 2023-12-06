#This is the final code of the class! Thanks for all your help!


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def calculate_wind_chill(temperature, wind_speed):
    """Calculate and return wind chill."""
    if temperature >= 50 or wind_speed < 5:
        return temperature  # No wind chill above 50°F or at low wind speeds
    else:
        wind_chill = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
        return wind_chill

temperature = float(input("What is the temperature? "))

scale = input("Fahrenheit or Celsius (F/C)? ").upper()

if scale == 'C':
    temperature = celsius_to_fahrenheit(temperature)

# Loop through wind speeds and calculate wind chill
print("\nWind Chill Calculation:")

for wind_speed in range(5, 61, 5):
    wind_chill = calculate_wind_chill(temperature, wind_speed)
    print(f"At temperature {temperature:.2f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

