print("""
-------------------------------------------------------
    The program below is to capture your basic information.
    Please enter the information carefully.
    NOTE: Press ENTER to go to the next question.
-------------------------------------------------------
""")

print('Name?')
name = input()
print('Age?')
age = input()
print('Height?')
height = input()
print('Gender?')
gender = input()
print('Occupation?')
occupation = input()

print("""
-------------------------------------------------------
    Below is what you have told us.
-------------------------------------------------------
""")
print('My name is ', name)
print('My age is', age)
print('My height is\\', height)
print('I\'m a', gender)
print('I work as', occupation)