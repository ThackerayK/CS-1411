#Kelly Thackeray
#Feb. 7, 2004
#To show a secondary color when two primary colors are mixed

#Declare variable
RED = 'red'
BLUE = 'blue'
YELLOW = 'yellow'

#Get input from the user
color1 = input('Enter the first primary color: ')
color2 = input('Enter the second primary color: ')

if color1 != RED and color1 != BLUE and color1 != YELLOW:
    print('The first color is invalid. ')
elif color2 != RED and color2 != BLUE and color2 != YELLOW:
    print('The second color is invalid. ')
elif color1 == color2:
    print('Both of the colors cannot be the same. ')
else:
    if color1 == RED:
        if color2 == BLUE:
            print('Purple')
        else:
            print('Orange')
    elif color1 == BLUE:
         if color2 == RED:
             print('Purple')
         else:
            print('Green')
    else:
        if color2 == RED:
             print('Orange')
        else:
            print('Green')
          
