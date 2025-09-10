def calculate(score: float) -> str:
    """Return letter grade for a numeric score between 0 and 100."""
    if 0 <= score <= 100:
        if score < 60:
            return "F"
        elif score < 70:
            return "D"
        elif score < 80:
            return "C"
        elif score < 90:
            return "B"
        else:
            return "A"
    else:
        return "N/A"

print(calculate(97.4))   
print(calculate(85))     
print(calculate(-1))    
print(calculate(120))    
