print('welcome')

score = 0

game_on = True

while game_on:

    play = input('would you like to play a game? ').lower()

    if play == 'yes':
        print('ready lets go')
    else:
        exit()

    answer = input('what is a gpu? ')
    if answer == 'graphics processing unit':
        score += 1
        print('correct')
    else:
        print('incorrect')

    answer = input('what is ram? ')
    if answer == 'random access memory':
        score += 1
        print('correct')
    else:
        print('incorrect')

    answer = input('what is a psu? ')
    if answer == 'power supply unit':
        score += 1
        print('correct')
    else:
        print('incorrect')

    answer = input('what is a cpu? ')
    if answer == 'central processing unit':
        score += 1
        print('correct')
    else:
        print('incorrect')

    answer = input("what is kyle's favourite bmw? ")
    if answer == 'M4':
        score += 1
        print('correct')
    else:
        print('incorrect')

    print(f'you answered {score} correctly')
    print('you got ' + str((score/5) * 100) + "%.")
    new_game = input('would you like to play again ?').lower()

    if new_game == 'yes':
        game_on = True
    else:
        break
