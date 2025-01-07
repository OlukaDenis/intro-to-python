print("what is your age?")
age = input()
if age.isdigit():
   formatted_age = int(age)
   if formatted_age >= 12:
      print("You're in adolescent stage")
   else:
      print("You're young")
else:
   print("age must be digits!!!")



print('What is your name?')
name = input()
print('What is your occupation?')
occupation = input()