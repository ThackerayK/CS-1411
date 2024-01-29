#Kelly Thackeray
#January 29, 2024
#To determine the future amount of a savings account

#Gather all the inputs
print('Enter the principle amount: ', end=' ')
p = float(input())

print('Enter the rate of interest: ',end=' ')
r = float(input())

print('Enter the compounding criteia: ',end=' ')
n = int(input())

print('Enter the time of the investment: ',end=' ')
t = int(input())

#Change rate of interest to a decimal
r = r / 100

#Calculate the future  amount
a = p * (1 + float (r) / n) ** (n*t)

#Calculate the interest earned
i = a - p

#Display the future amount
print('At the end of ' , t , 'years the future amount is $' , format(a, '.2f'))
print('At the end of ' , t , 'years, interest earned amount is $' , format(i, '.2f'))








                                         










