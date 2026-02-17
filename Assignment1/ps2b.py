
annual_salary   = float(input("Enter your annual salary: "))
portion_saved   = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost      = int(input("Enter the cost of your dream home: "))
semi_annualraise= float(input("Enter the semi-annual raise, as a decimal:"))

monthly_return=0.04/12
down_payment=0.25*total_cost
savings=0.0
months=0

monthly_salary=annual_salary/12

while savings<=down_payment:

    if (months%6==0 and months>0):
        annual_salary+=(annual_salary*semi_annualraise)
        monthly_salary=annual_salary/12
    savings+=savings*monthly_return    
    savings+=monthly_salary*portion_saved
    months+=1
print(f"no. of months to get your dream house:{months}")