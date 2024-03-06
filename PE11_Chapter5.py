#Kelly Thackeray
#March 4, 2024
#To determine the maximum of two integer values

def main():
    #Declare variable
    num1 = 0
    num2 = 0

    #User input
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))

    #Display
    print('The maximum is: ' , maximum(num1, num2))

def maximum(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2

main()
