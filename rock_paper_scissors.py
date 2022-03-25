import secrets
print('Welcome to the game! Good luck!')
while True:
    choice = input('Do you want to play a game? \nYes/No \n')
    if choice.title() == 'Yes' and 'No':
        choice_2 = input("\nPick Rock,Paper Or Scissors: ")
        options = ['Rock', 'Paper', 'Scissors']
        print(f'\nYou have picked {choice_2}')
        computer_choice = secrets.choice(options)
        if choice_2.title() == computer_choice:
            print(f"\nThe computer chooses {computer_choice}\nIt's a tie, play again!")
        elif choice_2.title() == "Rock":
            if computer_choice == "Scissors":
                print(f'\nThe computer choice is {computer_choice}\nRock smashes scissors! You win!')
            else:
                print(f'\nThe computer choice is {computer_choice}\nPaper defeats rock! You lose!')
        elif choice_2.title() == 'Paper':
            if computer_choice == 'Rock':
                print(f'\nThe computer choice is {computer_choice}\nPaper defeats rock! You win!')
            else:
                print(f'\nThe computer choice is {computer_choice}\nScissors defeat paper! You lose!')
        elif choice_2.title() == 'Scissors':
            if computer_choice == 'Paper':
                print(f'\nThe computer chose {computer_choice}\nScissor beats paper! You win!')
            else:
                print(f'\nThe computer choice is {computer_choice}\nRock smashes scissors! You lose')
        elif choice_2.title() and computer_choice is not options:
            print(f'Please pick a valid option from: ')
            for option in options:
                print(option)
    else:
        break
print('\nGAME OVER')











