import users

print("Please log in")
username = input("Username:")
if(username not in users.myusers):
    print('Username does not exist')
else:
    current_user = users.myusers[username]

    password = input("Password:")
    if current_user['password'] == password:
        print("Login successful")
        print("Welcome,", username)
        print("Name:", current_user['name'])
        print("Occupation:", current_user['occupation'])
    else:
        print('Incorrect password')

    