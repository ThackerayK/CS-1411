#Kelly Thackeray
#March 4, 2024
#Calculate grade based on 5 exams

def main():
    s1 = 0.00
    s2 = 0.00
    s3 = 0.00
    s4 = 0.00
    s5 = 0.00
    average = 0.00

    s1 = float(input('Enter the score for the first test: '))
    s2 = float(input('Enter the score for the second test: '))
    s3 = float(input('Enter the score for the third test: '))
    s4 = float(input('Enter the score for the fourth test: '))
    s5 = float(input('Enter the score for the fifth test: '))

    average = calc_average(s1, s2, s3, s4, s5)
    
    print('Score\t\tNumeric Score\tLetter Grade')
    print('--------------------------------------------------------------------')
    print('Score 1: \t\t' , s1, '\t\t' , determine_grade(s1))
    print('Score 2: \t\t' , s2, '\t\t' , determine_grade(s2))
    print('Score 3: \t\t' , s3, '\t\t' , determine_grade(s3))
    print('Score 4: \t\t' , s4, '\t\t' , determine_grade(s4))
    print('Score 5: \t\t' , s5, '\t\t' , determine_grade(s5))
    print('Average: \t\t' , average, '\t\t' , determine_grade(average))





def calc_average(score1, score2, score3, score4, score5):
    return (score1 + score2 + score3 + score4 + score5) / 5.00

def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


main()
