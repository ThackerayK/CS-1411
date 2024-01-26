

#Get input from the user
male_otters = float(input('Enter the number of males: '))
female_otters = float(input('Enter the number of females: '))

#Calculate
per_male = male_otters / (male_otters + female_otters)
per_female = female_otters / (male_otters + female_otters)

#Display
print(f'Percent males: {per_male:.0%}')
print(f'Percent female: {per_female:.0%}')
