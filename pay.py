import math

def unfair_weekly_paycheck_amount(hours_worked: float) -> int:
    return math.floor(hours_worked) * 15

hours = float(input("Enter hours: ")) 
print(unfair_weekly_paycheck_amount(hours))


def fair_weekly_paycheck_amount(hours_worked: float) -> float:
    return hours_worked * 15.0

hours = float(input("Enter hours: ")) 
print(f"{fair_weekly_paycheck_amount(hours):.2f}")
