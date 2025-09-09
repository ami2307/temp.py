 temp_fahrenheit = float(input("Enter temperature in Fahrenheit:-"))
def in_celsius(F):
    C=(5/9)*(F - 32)
    TEMP = C
    return TEMP
print("Temperature in Celsius:",in_celsius(temp_fahrenheit))
