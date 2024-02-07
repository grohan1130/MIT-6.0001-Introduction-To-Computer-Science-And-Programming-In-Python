"""""
Rohan Gupta
MIT OCW - 6.0001
Problem Set 1 - Part B
"""""

# prompt user inputs
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the portion of your salary you plan to save each month: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

# additional variables
portion_down_payment = 0.25
total_down_payment_amount = total_cost * portion_down_payment
annual_return_rate = 0.04
current_savings = 0
months_taken = 0
monthly_savings = (annual_salary / 12) * portion_saved

# calculate number of months to reach down payment value in savings
while current_savings < total_down_payment_amount:
    current_savings += (current_savings * 0.04/12) + monthly_savings 
    months_taken += 1
    if months_taken % 6 == 0:
        monthly_savings += monthly_savings * semi_annual_raise

print("Number of months: ", months_taken)





