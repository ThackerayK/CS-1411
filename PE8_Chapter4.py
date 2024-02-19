#Kelly Thackeray
#Feb. 19, 2024
#Use of a sentinel and the accumulator

#Declare the variables
number = 1.00
total = 0.00

while number > 0.00:
    number = float(input("Enter a positive number: "))
    if number > 0.00:
        total += number

print("The total equals" , format(total, " .2f"))
