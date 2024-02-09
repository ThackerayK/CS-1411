#This program calculates whether the product of the month and day equal the year

#Declare variable and get user input
month = int(input('Enter the month (numeric): '))
day = int(input('Enter the day: '))
year = int(input('Enter the last two digits of the year: '))

#Calculate
if month * day == year:
    print('This date is magic!')
else:
    print('This date is not magic.')
