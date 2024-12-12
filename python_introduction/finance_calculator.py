monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses:")

monthly_savings = int(monthly_income) - int(monthly_expenses)

projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Enter your monthly income: " ,monthly_income)
print("Enter your total monthly expenses: " ,monthly_expenses)
print("Your monthly savings are $",monthly_savings,".")
print("Projected savings after one year, with interest, is: $",projected_Savings,".")