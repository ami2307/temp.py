temp_fahrenheit_input = input("Enter temperature in Fahrenheit: ")
temp_fahrenheit = float(temp_fahrenheit_input)
def fahrenheit_to_celsius(fahrenheit: float) -> float:
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)
print(f"Temperature in Celsius: {temp_celsius}")

