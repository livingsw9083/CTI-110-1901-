# For this project, I had to make a program where whenever I put in the amount
# for total sales, it would give me the amount of profit made from it.
# June 23, 2020
# CTI-110 P2T1-Sales Prediction
# Will Livingston
#


# Get the projected total sales
total_sales= float(input('Enter the projected sales:'))

# Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))

