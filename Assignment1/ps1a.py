# Getting the required input from the user
annual_salary   = float(input("Enter your annual salary: "))
portion_saved   = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost      = float(input("Enter the cost of your dream home: "))

# Calculating monthly return on investment since we need to find the number of months
monthly_return=0.04/12
# Calculating the down payment required
down_payment=0.25*total_cost
# Initial savings is zero
savings=0.0
# Initial number of months is zero
months=0
# Taking mothly salary so that monthly return can be applied
monthly_salary=annual_salary//12

# When savings equals downpayment the loop needs to stop
while savings<down_payment:
    months+=1
    
    savings+=savings*monthly_return    
    savings+=monthly_salary*portion_saved

    
print(f"no. of months to get your dream house:{months}")
