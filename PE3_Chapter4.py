#Kelly Thackeray
#Feb. 14, 2024
#Budget analysis, loop to display the amount over or under budget

#Declare variables
amount_budgeted = 0.00
total =0.00
difference = 0.00

#Initialization for the while loop
amount_spent = 1.00

#Gather input from the user
amount_budgeted = float(input('Enter the amount for the month: '))

while amount_spent != 0.00:
     amount_spent = float(input('Enter the amount spent: '))
     total += amount_spent
print('Amount budgeted: $' , format(amount_budgeted, '.2f'))
print('Amount spent: $' , format(total, '.2f'))

if amount_budgeted > total:
    difference = amount_budgeted - total
    print('You are $' , format(difference, '.2f'), 'under the budget.')
elif amount_budgeted < total:
    difference = total - amount_budgeted
    print('You are $' , format(difference, '.2f'), 'over the budget.')
else:
    print("You broke even")
 
    


