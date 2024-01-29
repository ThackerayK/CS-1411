#Kelly Thackeray
#January 29, 2024
#To determine the profit/loss in stocks

#Declare constants
NUM_OF_SHARES = 2000
PURCHASE_PRICE = 40.00
SELLING_PRICE = 42.75
COMMISSION_RATE = 0.03

#Declare variables
amount_Paid = 0.00
commission_paid_buying = 0.00
total_paid_buying = 0.00
amount_received = 0.00
commission_paid_selling = 0.00
total_received_selling = 0.00
profit_loss = 0.00

#Amount paid buying
amount_paid = NUM_OF_SHARES * PURCHASE_PRICE

#Commission paid buying
commission_paid_buying = amount_paid * COMMISSION_RATE

#Total paid buying
total_paid_buying = amount_paid + commission_paid_buying

#Amount received selling
amount_received = NUM_OF_SHARES * SELLING_PRICE

#Commission paid selling
commission_paid_selling = amount_received * COMMISSION_RATE

#Total_Received Selling
total_received_selling = amount_received - commission_paid_selling

#Profit or loss
profit_loss = total_received_selling - total_paid_buying

print('Amount paid: $', format(amount_paid, '.2f'))
print('Commission paid buying: $' ,format(commission_paid_buying,' .2f'))
print('Amount selling: $', format(amount_received,' .2f'))                                           
print('Commission paid selling: $', format(commission_paid_selling,' .2f'))
print('Profit or loss: $', format(profit_loss,' .2f'))                                           










