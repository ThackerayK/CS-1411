#Kelly Thackeray
#Feb.12, 2024
#To calculate the number of points awarded based on the number of books purchased

#Declare variables
number_of_books = 0
points_awarded = 0

#Gather input from the user
number_of_books = int(input('Enter the number of books purchased: '))

#Award points
if number_of_books == 2:
    points_awarded = 5
elif number_of_books == 4:
    points_awarded = 15
elif number_of_books == 6:
    points_awarded = 30
elif number_of_books >= 8:
    points_awarded = 60
else:
    points_awared = 0
print('You have purchased' ,number_of_books, 'books. ')
print('You have earned' , points_awarded, 'points. ')
