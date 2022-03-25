def password_checker(password):
    digit_counter = 0
    lower_counter = 0
    upper_counter = 0
    length_counter = 0
    special_counter = 0
    if len(password) >= 8:
        length_counter += 1
    for x in password:
        if x.isdigit():
            digit_counter += 1
        elif x.isupper():
            upper_counter += 1
        elif x.islower():
            lower_counter += 1
        elif x == '_' or x == '@' or x == '$' or x == '#':
            special_counter += 1
    return digit_counter, lower_counter, upper_counter, length_counter, special_counter
list = []
while True:
    print('This program checks that your password has the following:\n1) At least 8 characters\n2) At least one digit\n3) At least one uppercase character\n4) At least One lowercase character'
          '\n5) At least one special character (@, _, $, #)')
    password_input = input("Enter the password (press 'exit' to finish the program or 'list' to see the saved passwords) ")
    num_digits, num_lower, num_upper, num_length, num_special = password_checker(password_input)
    if password_input.upper() == 'exit'.upper():
        break
    if num_digits >= 1 and num_lower >= 1 and num_length >= 1 and num_special >= 1 and num_upper >= 1:
        print(f"The password '{password_input}' is valid")
        list.append(password_input)
    elif password_input == 'list':
        print(list)
    else:
        print(f"The password '{password_input}' is not valid. Try again")











