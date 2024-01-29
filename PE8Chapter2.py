
#Kelly Thackeray
#January 24,2024
#To calculate the total bill at a restaurant.

# Declare variable
food_cost = 0.00
tip_amount = 0.00
tax_amount = 0.00
total_bill = 0.00
sub_total = 0.00

#Declare constants
TAX_RATE = 0.0825
TIP_RATE = 0.15

#Get the cost of the items ordered
food_cost = float(input("Enter the cost of the food: "))

#Calculate the tax
tax_amount = food_cost * TAX_RATE

#Calculate the subtootal
sub_total = food_cost + tax_amount

#Calculate the tip
tip_amount = sub_total * TIP_RATE

#calculate the total bill
total_bill = sub_total + tip_amount

#print tax, tip, and total bill
print("Tax: $", format(tax_amount, '.2f'))
print("Tip: $", format(tip_amount, '.2f'))
print("Total: $", format(total_bill, '.2f'))
