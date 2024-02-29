#Kelly Thackeray
#Feb. 28, 2024
#How many tickets for each class of seat and calculate costs

#Declare Constants
CLASS_A = 25.00
CLASS_B = 20.00
CLASS_C = 15.00

def main():
    seatA = 0
    seatB = 0
    seatC = 0
    revenueA = 0.00
    revenueB = 0.00
    revenueC = 0.00

    seatA = int(input("Enter the number of class A seats sold: "))
    seatB = int(input("Enter the number of class B seats sold: "))
    seatC = int(input("Enter the number of class C seats sold: "))

    revenueA = seatA * CLASS_A
    revenueB = seatB * CLASS_B
    revenueC = seatC * CLASS_C

    ticket_costs(revenueA, revenueB, revenueC)




def ticket_costs(revA, revB, revC):
    total_rev = 0.00
    total_rev = revA + revB + revC
    print("Revenue from Class A tickets: $" , format(revA , ".2f"), sep = " ")
    print("Revenue from Class B tickets: $" , format(revB  ,".2f"), sep = " ")
    print("Revenue from Class C tickets: $" , format(revC  ,".2f"), sep = " ")
    print("Total revenue is: $ ", format(total_rev, " .2f"), sep = " ")


    


main()
