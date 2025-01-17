# Local Scope - They are only accessible within that function's body and are destroyed once the function execution completes.
# Enclosing scope - 
# Global scope
# Built in scope


dob = 1990 # global scope

def myAge():
    age = 2025 - dob # local scope
    print(age)

    def myGeneration():
        name = 'Denis' # local scope
        print('Gen Z')
