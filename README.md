# temp.py
Converting temperature in Fahrenheit from Celsius 

temp_fahrenheit = float(input("Enter temperature in Fahrenheit:-"))

-> Displays a message asking the user to enter a temperature in Fahrenheit.

-> Reads the input as a string, then converts it to a floating-point number using float().

-> in_celsius(F) is a function that takes a Fahrenheit value F as its parameter.

-> Inside the function, it uses the formula for Fahrenheit to Celsius conversion:
C = 5/9 (F − 32)

-> The result C (Celsius temperature) is stored in the variable TEMP and returned.

print("Temperature in Celsius:", in_celsius(temp_fahrenheit))

-> This prints the Celsius temperature by calling the conversion function with the user's input.

-> The function calculates and returns the Celsius value, which gets printed.
