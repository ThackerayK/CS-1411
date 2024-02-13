#Kelly Thackeray
#Feb.12, 2024
#Display a discount and the total amount based on the number of packages ordered

#Declare constant
RETAIL_PRICE = 99.00

#Declare variables
packages_ordered = 0
full_price = 0.00
discount_percentage = 0.00
discount_amount = 0.00
total_amount = 0.00

#Gather input from the user
packages_ordered = int(input('Enter the number of packages ordered: '))

#Calculate the discount rate
if packages_ordered > 99:
    discount_percentage = 0.40
elif packages_ordered > 49:
    discount_percentage = 0.30
elif packages_ordered > 19:
    discount_percentage = 0.20
elif packages_ordered > 9:
    discount_percentage = 0.10
else:
    discount_percentage = 0.00

#Calculate the full price
full_price = RETAIL_PRICE * packages_ordered

#Calculate the discount
discount_amount = full_price * discount_percentage

#Calculate the full amount
total_amount = full_price - discount_amount

#Display discount and total
print('Discount amount: $' , format(discount_amount, '.2f'))
print('Total amount: $' , format(total_amount, '.2f'))


                                    
