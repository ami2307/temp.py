def calculate(score):
    if 0 <= score <= 100:
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    else:
        return "N/A"

grade_input = input("Enter the score: ")
try:
    grade = float(grade_input)
    print("Grade:", calculate(grade))
except ValueError:
    print("Invalid input! Please enter a number between 0 and 100.")
