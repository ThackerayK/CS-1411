#Kelly Thackeray
#Feb. 19, 2024
#Calculate the salary in pennies

#Declare the variables
pennies_per_day = 1
number_of_days = 0
total_pay = 0.00

#Get the input from the user
number_of_days = int(input("Enter the numbers of days you wish to work: "))

#Display a table.
print("Day\tPennies")
print("----------------------")

for day in range(1, number_of_days + 1):
     print(day, '\t$' , float(pennies_per_day /100))
     total_pay += pennies_per_day
     pennies_per_day *= 2

#Display the total pay
print("The total pay for" ,  number_of_days, "days is $" , float(total_pay/100))
    
