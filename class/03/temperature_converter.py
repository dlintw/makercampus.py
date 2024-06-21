def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

temp_in_fahrenheit = 98.6
temp_in_celsius = fahrenheit_to_celsius(temp_in_fahrenheit)
print(f"{temp_in_fahrenheit} °F = {temp_in_celsius:.2f} °C")

temp_in_celsius = 37
temp_in_fahrenheit = celsius_to_fahrenheit(temp_in_celsius)
print(f"{temp_in_celsius} °C = {temp_in_fahrenheit:.2f} °F")
