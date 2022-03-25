name = input('What is your name to start the game: ')

choices = ['"Door1: Giant Spider"', '"Door2: Octopus with Chainsaws"', '"Door3: Dragon"']

print(f"Hi {name}, let's see if you can win this decision making game.\n\nYou are sitting in a dark room.\nThere are three doors in front of you with the following signs: ")

for x in choices:
    print(x)

choice = input('Which door do you want to pick 1, 2, or 3 : ')
if choice == '1':
    print(f'\nBad choice {name}! The spider trapped you into his web an ate you alive!\n\nGAME OVER!')

elif choice == '2':
    print(f'\nBad choice {name}! The octopus slashed you into thousand tiny little pieces!\n\nGAME OVER!')

else:
    print(f"\nRight choice {name}! Let's play a game!")
    print(f"OK {name}, you have 2 choices now:\n1) You can pick a sword and kill the {choices} dragon\n2) Talk to the dragon and befriend him")

    choice_2 = input(f'Which one do you want to pick {name}, 1 or 2? ')
    if choice_2 == '1':
        print(f'\nThis is the right choice {name}, this dragon is unpredictable and dangerous!\n\nCONGRATULATIONS, YOU WON')

    else:
         print(f'\nThat was a terrible choice {name}! The dragon was starving for days and you served as the perfect snack!\n\nYou lost the game. \n\nGAME OVER!')
