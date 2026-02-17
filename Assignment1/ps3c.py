# Getting the required input from the user
starting_salary = float(input("Enter the starting salary: "))
down_payment = 1000000 * 0.25
Raise = 0.07
ROI = 0.04
MONTHS = 36


def check_savings(rate):       
    savings = 0.0
    salary = starting_salary
    for m in range(1, MONTHS + 1):
        savings += savings * (ROI / 12) + (salary / 12) * (rate / 10000)
        if m % 6 == 0: salary += salary * Raise
    return savings

# Using bisection search
low=0 
high=10000
steps = 0
while low <= high:
    steps += 1
    mid = (low + high) // 2
    total_saved = check_savings(mid)
    
    if abs(total_saved - down_payment) <= 100: 
        print(f"Best savings rate: {mid/10000:.4f}\nSteps in bisection search: {steps}")
        break
    elif total_saved < down_payment: low = mid + 1
    else: high = mid - 1
    
    if low > 10000: 
        print("It is not possible to pay the down payment in three years.")
        break
