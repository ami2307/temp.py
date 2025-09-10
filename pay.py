import math

def unfair_weekly_paycheck_amount(hours_worked: float) -> int:
    return math.floor(hours_worked) * 15

if __name__ == "__main__":
    hours = float(input())
    print(unfair_weekly_paycheck_amount(hours))

def fair_weekly_paycheck_amount(hours_worked: float) -> float:
    return hours_worked * 15.0

if __name__ == "__main__":
    hours = float(input())
    print(f"{fair_weekly_paycheck_amount(hours):.2f}")


