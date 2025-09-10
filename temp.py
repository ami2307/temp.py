temp_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
def fahrenheit_to_celsius(temp_fahrenheit: float) -> float:
    return (temp_fahrenheit - 32) * 5.0 / 9.0

if __name__ == "__main__":
    temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)
    print(f"Temperature in Celsius: {temp_celsius}")

