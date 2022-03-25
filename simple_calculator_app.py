import secrets
print('Welcome to the calculator app!')
def addition(value, value_1):
    print('This is addition')
    result = value + value_1
    return result
def subtraction(value, value_1):
    print('This is subtraction')
    result = value - value_1
    return result
def multiplication(value, value_1):
    print('This is multiplication')
    result = value * value_1
    return result
def division(value, value_1):
    print('This is division')
    result = value / value_1
    return result
def power(value, value_1):
    print('The value is a power')
    result = value ** value_1
    return result
while True:
    ask_user = input('What you want to do?\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Power\n6.Random selection\n7.Exit\n')
    if ask_user == '1':
        number_1 = int(input('First number: '))
        number_2 = int(input('Second number: '))
        calculation = addition(number_1, number_2)
        print(f'The result is {calculation}')
    elif ask_user == '2':
        number_1 = int(input('First number: '))
        number_2 = int(input('Second number: '))
        calculation = subtraction(number_1, number_2)
        print(f'The result is {calculation}')
    elif ask_user == '3':
        number_1 = int(input('First number: '))
        number_2 = int(input('Second number: '))
        calculation = multiplication(number_1, number_2)
        print(f'The result is {calculation}')
    elif ask_user == '4':
        number_1 = int(input('First number: '))
        number_2 = int(input('Second number: '))
        calculation = division(number_1, number_2)
        print(f'The result is {calculation}')
    elif ask_user == '5':
        number_1 = int(input('First number: '))
        number_2 = int(input('Second number: '))
        calculation = power(number_1, number_2)
        print(f'The result is {calculation}')
    elif ask_user == '6':
        computer_choice = secrets.choice(['1','2','3','4','5'])
        print(f'Computer choice is, {computer_choice}')
        if computer_choice == '1':
            number_1 = int(input('First number: '))
            number_2 = int(input('Second number: '))
            calculation = addition(number_1, number_2)
            print(f'The result is {calculation}')
        elif computer_choice == '2':
            number_1 = int(input('First number: '))
            number_2 = int(input('Second number: '))
            calculation = subtraction(number_1, number_2)
            print(f'The result is {calculation}')
        elif computer_choice == '3':
            number_1 = int(input('First number: '))
            number_2 = int(input('Second number: '))
            calculation = multiplication(number_1, number_2)
            print(f'The result is {calculation}')
        elif computer_choice == '4':
            number_1 = int(input('First number: '))
            number_2 = int(input('Second number: '))
            calculation = division(number_1, number_2)
            print(f'The result is {calculation}')
        elif computer_choice == '5':
            number_1 = int(input('First number: '))
            number_2 = int(input('Second number: '))
            calculation = power(number_1, number_2)
            print(f'The result is {calculation}')
    elif ask_user == '7':
        print('Exiting the calculator')
        break
    else:
        print('This is not an option, try again!')






