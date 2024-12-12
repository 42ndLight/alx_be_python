income = input("Enter your monthly income: ")
expenses = input("Enter your total monthly expenses:")

savings = int(income) - int(expenses)

Projected_Savings = savings * 12 + (savings * 12 * 0.05)

print("Enter your monthly income: " ,income)
print("Enter your total monthly expenses: " ,expenses)
print("Your monthly savings are $",savings,".")
print("Projected savings after one year, with interest, is: $",Projected_Savings,".")