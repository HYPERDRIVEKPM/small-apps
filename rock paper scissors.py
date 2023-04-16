from random import randint

print('welcome to rock, paper, scissors\n')

player_wins = 0
cpu_wins = 0

options = ['rock', 'paper', 'scissors']

while True:

    player_choice = input('please enter a choice : rock/paper/scissors or q to exit: ').lower()

    if player_choice == 'q':
        break

    if player_choice not in ['rock', 'paper', 'scissors']:
        continue

    number = randint(0, 2)

    cpu_guess = options[number]

    if player_choice == 'rock' and cpu_guess == 'scissors':
        player_wins += 1
        print('player wins!')
        print(f'you choose {player_choice} and cpu choice {cpu_guess}')
        print(f'player has won {player_wins}')

    elif player_choice == 'paper' and cpu_guess == 'rock':
        player_wins += 1
        print('player wins!')
        print(f'you choose {player_choice} and cpu choice {cpu_guess}')
        print(f'player has won {player_wins}')

    elif player_choice == 'scissors' and cpu_guess == 'paper':
        player_wins += 1
        print('player wins!')
        print(f'you choose {player_choice} and cpu choice {cpu_guess}')
        print(f'player has won {player_wins}')

    elif player_choice == cpu_guess:
        print('game is a tie! ')
        print(f'you choose {player_choice} and cpu choice {cpu_guess}')

    else:
        cpu_wins += 1
        print('cpu wins!')
        print(f'you choose {player_choice} and cpu choice {cpu_guess}')
        print(f'cpu has won {cpu_wins} games')
    play_again = 'wrong'

    while play_again not in ['yes', 'no']:

        play_again = input('would you like to play again? yes - no ').lower()

        if play_again == 'yes':
            continue
        elif play_again == 'no':
            quit()
        else:
            print('please enter a valid choice')
