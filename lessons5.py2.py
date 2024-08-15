def calculate():
    while True:
        num1 = float(input('Enter first number: '))
        operator = input('Enter operator (+, -, *, /): ')
        num2 = float(input('Enter second number: '))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print('Cannot divide by zero')
                continue
            result = num1 / num2
        else:
            print('Invalid operator')
            continue

        print(f'The result is {result}')

        continue_calc = input('Do you want to continue? (y/yes to continue): ').lower()
        if continue_calc not in ['y', 'yes']:
            print('Goodbye!')
            break

calculate()