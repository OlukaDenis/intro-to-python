def myFunction(number):
    # one = 'denis'
    # two = 'henry'
    if(number % 2 == 0):
        raise ValueError('We only accept odd numbers')
    
    return 'Success'

try:
    print(myFunction(4))
except ValueError as e:
    print(str(e))
except TypeError:
    print('Inappropriate type is applied to the function.')
except ArithmeticError:
    print('Mathematical error has aoccured') 
except Exception:
    print('Unknown error occurred.')        