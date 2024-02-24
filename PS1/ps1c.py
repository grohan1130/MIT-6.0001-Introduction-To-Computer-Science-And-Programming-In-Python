"""""
Rohan Gupta
MIT OCW - 6.0001
Problem Set 1 - Part C
"""""

# prompt user inputs
annual_salary = float(input('Enter your annual salary: '))

# starting variables
total_cost = 1000000
down_payment_portion = 0.25
target_savings = total_cost * down_payment_portion

annual_investment_return_rate = 0.04
monthly_investment_return_rate = annual_investment_return_rate / 12

monthly_salary = annual_salary / 12
semi_annual_raise_rate = 1.07
salary_saved_portion = 0.0


def get_total_savings(monthly_salary, semi_annual_raise_rate, salary_saved_portion):
    total_savings = 0
    for month in range(36):
        total_savings += (total_savings * monthly_investment_return_rate) + (monthly_salary * salary_saved_portion)
        if (month + 1) % 6 == 0:
            monthly_salary = monthly_salary * semi_annual_raise_rate
    return(total_savings)

lower_bound = 0.0
upper_bound = 1.0
success = False

if (get_total_savings(monthly_salary, semi_annual_raise_rate, 1.0)) < target_savings:
    success = True
    print("It is not possible to pay the down payment in three years")

num_guesses = 1
while success == False:
    salary_saved_portion = (lower_bound + upper_bound)/2
    num_guesses += 1
    total_savings = get_total_savings(monthly_salary, semi_annual_raise_rate, salary_saved_portion)
    if abs(total_savings - target_savings) <= 100:
        print(f'Guess {num_guesses}: Optimal savings rate  is {salary_saved_portion}')
        success = True
        break
    else: 
        if target_savings - total_savings > 100:
            lower_bound = salary_saved_portion
        else:
            upper_bound = salary_saved_portion




