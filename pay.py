import math
hours = float(input("hours of work : "))
def unfair_weekly_paycheck_amount(hours_work):
    unfair_hours = 0
    unfair_hours = math.floor(hours_work)
    unfair_pay = unfair_hours * 15
    return f"If you work {hours_work} hours, you are paid ${unfair_pay}"
def fair_weekly_paycheck_amount(hours_work):
    fair_pay = hours_work * 15
    return f"If you work {hours_work} hours, you are paid $ {fair_pay}"
print(unfair_weekly_paycheck_amount(hours))
print(fair_weekly_paycheck_amount(hours))