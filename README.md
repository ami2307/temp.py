Ami Raj ami.raj2307@gmail.com

1) print vs. return
The print statement displays output to the console, while return sends a value back from a function for further use.
Example:
def my_function():
    print("Ami")    # Shows "Ami" in the console
    return "Ami"    # Returns "Ami" to where function was called

3) bugs and issues
When I ran my Python program, it crashed if I entered a non-numeric value instead of a number. This was because the input was not being validated correctly.

4) resolved issue
To fix the error, I added a check to make sure the input is numeric before processing it. Now, the program gives a clear message if the input is invalid and keeps running smoothly.
