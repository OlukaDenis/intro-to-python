""" This module describes the use of arguments in functions."""

def age(currentYear, birthYear = 2000):
    """ 
    This function calculates a person's age. 
    It accepts two arguments, currentYear and birthYear
    """
    return currentYear - birthYear;

def add_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total