import keyword
import string

def is_valid_variable_name(name):
    if name in keyword.kwlist or name [0].isdigit():
        return False

    for char in name:
        if char.isupper() or (char in string.punctuation and char !='_'):
            return False

    if name.count('_') > 1 and name.strip('') =='':
        return False

    return True

user_input = input("Enter a variable name: ")
print(is_valid_variable_name(user_input))
