#Constant Variable
COOKIES = 48
SUGAR = 1.5
BUTTER = 1
FLOUR = 2.75

#Ask the user for the number of cookies
num_cookies = float(input('Please enter the number of cookies you would like to bake: '))

#Calculate
sugar_cups = (num_cookies/COOKIES)*SUGAR
butter_cups = (num_cookies/COOKIES)*BUTTER
flour_cups = (num_cookies/COOKIES)*FLOUR

#Display
print(f'For {num_cookies} cookies, you will need: '
          f'{sugar_cups} cups of sugar, '
          f'{butter_cups} cups of butter, and '
          f'{flour_cups} cups of flour.')
