#Kelly Thackeray
#January 22, 2024
#To compute the total price of an item

#Declare variables
purchase = 0.0
state_tax = 0.00
county_tax = 0.00
total_tax = 0.00
total_price = 0.00


#Delare constants
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

#Gather the input from the user
purchase = float(input("Enter the purchse price of an item: "))

#Calculate the state tax
state_tax = purchase * STATE_TAX_RATE

#Calculate the county tax
county_tax = purchase * COUNTY_TAX_RATE

#Calculate the total tax
total_tax = state_tax + county_tax

#Calculate the total price
total_price = purchase + total_tax

 #Display the output
print("Purchase Price:$" , format(purchase, '.2f'))
print("Sate Tax:$" , format(state_tax, '.2f'))
print("County Tax:$" , format(county_tax, '.2f'))
print("Total Tax:$" , format(total_tax, '.2f'))
print("Total Price: $" , format(total_price, '.2f'))

 
