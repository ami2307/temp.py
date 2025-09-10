import math

def unfair_weekly_paycheck_amount(hours_worked: float) -> int:
    return math.floor(hours_worked) * 15

def fair_weekly_paycheck_amount(hours_worked: float) -> float:
    return hours_worked * 15.0

print("Unfair Pay:")
print(unfair_weekly_paycheck_amount(2))       
print(unfair_weekly_paycheck_amount(2.5))     
print(unfair_weekly_paycheck_amount(100.75))  

print("\nFair Pay:")
print(fair_weekly_paycheck_amount(2))         
print(fair_weekly_paycheck_amount(2.5))       
print(fair_weekly_paycheck_amount(100.75))   
