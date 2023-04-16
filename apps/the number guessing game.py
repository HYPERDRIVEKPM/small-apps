from random import randint

print('welcome to the number guessing game \n')

while True:

    guess_count = 0

    r = randint(0, 10)

    start = '1'

    while start not in ['yes', 'no']:

        start = input('are you ready to start the game? yes - no ').lower()

        if start == 'yes':
            pass
        elif start == 'no':
            quit()
        else:
            print('please enter a valid choice yes - no ')

    game_on = True

    while game_on:

        guess_count += 1

        player_guess = input('please enter a choice from 1 - 10 ')

        if player_guess.isdigit():
            player_guess = int(player_guess)

            if player_guess < 0:
                print('please enter a number between 0 - 10 ')
                game_on = True

        else:
            print('please enter a number!')
            game_on = True

        if player_guess == r:
            print(f'correct your guess was {player_guess} and the random number is {r}')
            if guess_count > 1:
                print(f'you took {guess_count} guesses')
                break
            else:
                print('incredible you got it on the first guess :) ')
                break

        else:
            print('incorrect')
            if player_guess > r:
                print(f'number is lower then {player_guess}')
            else:
                print(f'number is higher then {player_guess}')

    play_again = True

    while play_again:

        play_again = input('Would you like to play again? yes - no ').lower()

        if play_again == 'yes':
            play_again = False
            break
        elif play_again == 'no':
            quit()
        else:
            print('please enter a valid option yes - no ')
