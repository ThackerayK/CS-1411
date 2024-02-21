#Kelly Thackeray
#Feb. 21, 2024
#Calculate a positive factorial integer

#Declare variables
num = 0
factorial = 1 #accumulator

#Get the input from the user. While loop for input validation.
while num <= 0:
    num = int(input("Enter a nonnegative integer: "))

for fact in range(1, num + 1):
    factorial *= fact

#Display the factorial
print("The factorial of " , num, "is" , factorial)
