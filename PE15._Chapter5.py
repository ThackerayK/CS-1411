#Kelly Thackeray
#March 18, 2024
#Determine even or odd random numbers

import random

def main():
    number = 0
    evenCounter = 0
    oddCounter = 0
    totalNumbers = 100

    for i in range(totalNumbers):
        number = random.randint(1, 100)
        if isEven(number):
            evenCounter += 1
        else:
            oddCounter += 1
            
    print('Out of ' , totalNumbers, 'random numbers,' , evenCounter, 'were even, and' , oddCounter, 'were odd.')
    


def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

main()
    
