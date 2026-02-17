# ---------- get all parameters from the user ----------
starting_salary   = float(input("Enter the starting annual salary: "))
house_cost        = float(input("Enter the house cost: "))
down_payment  = float(input("Enter the down‑payment percent: "))
annual_return     = float(input("Enter the annual return on investment (as a decimal, e.g., 0.04): "))
semi_raise        = float(input("Enter the semi‑annual raise: "))


# ---------- derived constants ----------
down_payment   = down_payment * house_cost
monthly_return = annual_return / 12 
monthly_salary= starting_salary/12


# ---------- helper: simulate 36‑month savings for a given rate ----------
def simulate(rate):
    salary = starting_salary
    saved  = 0.0
    for m in range(1, 37):
        saved += (salary / 12) * rate          # monthly contribution
        saved += saved * monthly_return        # interest earned
        if m % 6 == 0:                         # apply raise every 6 months
            salary *= (1 + semi_raise)
    return saved

# ---------- first, see if the goal is even possible ----------
if simulate(1.0) < down_payment - tolerance:
    print("It is not possible to pay the down payment in the given time.")
else:
    # ---------- bisection search ----------
    low   = 0.0          # 0 % of salary saved
    high  = 1.0          # 100 % of salary saved
    steps = 0

    while True:
        steps += 1
        guess = (low + high) / 2
        saved = simulate(guess)

        # difference between what we saved and what we need
        diff = saved - down_payment

        # stop when we are within the $tolerance window
        if diff <= tolerance and diff >= -tolerance:
            break                     # success

        # otherwise shrink the interval
        if diff < -tolerance:         # saved too little → need a larger rate
            low = guess
        else:                         # saved too much → rate is too high
            high = guess

        # safety net: if interval gets extremely tiny, stop anyway
        if high - low < 1e-7:
            break

    print(f"Best savings rate: {guess:.4f}")
    print(f"Steps in bisection search: {steps}")