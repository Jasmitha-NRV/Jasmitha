
annual_salary   = float(input("Enter your annual salary: "))
portion_saved   = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost      = float(input("Enter the cost of your dream home: "))

monthly_return=0.04/12
down_payment=0.25*total_cost
savings=0.0
months=0

monthly_salary=annual_salary//12

while savings<=down_payment:
    months+=1
    
    savings+=savings*monthly_return    
    savings+=monthly_salary*portion_saved

    
print(f"no. of months to get your dream house:{months}")