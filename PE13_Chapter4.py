#Kelly Thackeray
#Feb. 21, 2024
#Use nested loops to draw a pattern of seven rows of stars.

#Define the character to print
character = " * "

#Number of rows and columns
size = 7

#Use a nested loop to iterate
for row in range(size):
    for col in range(size, row, - 1):
        print(character, end=' ')
    print()
