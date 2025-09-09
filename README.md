# Assignment 1

1) "Converting temperature in Fahrenheit from Celsius"

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

2) "Computing wages in two ways"

-> The code starts by importing the math module for advanced math functions.
-> It then collects user input for hours worked: hours = float(input("hours of work :"))
     This line prompts for a number, accepts input as a string, and converts it to a float for calculations.

  Unfair Weekly Paycheck
  -> math.floor(hours_work) always rounds down to the nearest integer.
  -> Pay is only calculated for these "whole" hours: unfair_pay = unfair_hours × 15
  
  Fair Weekly Paycheck
  -> It multiplies the total hours (including decimals) by 15 to give the full amount earned.
