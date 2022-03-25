usernames = ''
while True:
    user_input = input('What do you want to do? \n1) See the usernames stored in the source file\n2) Add username to the file\n3) Exit\n')
    if user_input == '1':
        try:
            with open('usernames.txt') as f:
                contents = f.readlines()
                for line in contents:
                    print(line.rstrip())
        except FileNotFoundError:
            print('The file does not exist')
    elif user_input == '2':
        username_input = input('Which username you want to add: \n')
        with open('usernames.txt', 'a') as file_object:
            file_object.write(f'{username_input}\n')
            print(f'Correctly added {username_input}')
    elif user_input == '3':
        break
    else:
        break
