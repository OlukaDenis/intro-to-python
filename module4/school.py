from calculator import subtraction
import calculator as calc
import my_arguments
import random
# import arrow

girls = 1000
boys = 4500

population = calc.addition(girls, boys)
print('Our school population is: ', population)

myAge = my_arguments.age(currentYear=20204, birthYear=2026)
print('My age is: ', myAge)

total = my_arguments.add_numbers(1,2.0,3,1.4,5,6,7.89,8)
print('Total: ', total)

myRandom = random.randint(10, 5000)
print('Random: ', myRandom)


# birth = arrow.get(2005, 3, 14)
# birth.humanize()