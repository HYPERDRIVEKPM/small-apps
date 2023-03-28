from random import randint


def display_board(board):
    print('' + board[7] + '|' + board[8] + '|' + board[9])
    print('' + board[4] + '|' + board[5] + '|' + board[6])
    print('' + board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    marker = ' '

    while marker not in ['X', 'O']:
        marker = input('please enter a choice X - O : ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def win_check(board, marker):
    return ((board[7] == board[8] == board[9] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[1] == board[2] == board[3] == marker) or
            (board[1] == board[4] == board[7] == marker) or
            (board[2] == board[5] == board[8] == marker) or
            (board[3] == board[6] == board[9] == marker) or
            (board[1] == board[5] == board[9] == marker) or
            (board[3] == board[5] == board[7] == marker))


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
        # board is full if we return True
    return True


def player_pos(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('please enter a position from 1 - 9 :'))

    return position


def replay():
    choice = 'wrong'

    while choice not in ['Y', 'N']:
        choice = input('would you like to play again please enter a option Y - N :').upper()

    if choice == 'Y':
        return True
    else:
        return False


def choose_first():
    if randint(0, 1) == 0:
        return 'player 1'
    else:
        return 'player 2'


def place_marker(board, marker, position):
    board[position] = marker

def tic_tac_toe():

    print("Welcome to tic tac toe")

    while True:

        board = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + " will go first")

        play_game = 'wrong'

        while play_game not in ['Y', 'N']:

            play_game = input("would you like to play a game Y - N : ").upper()

            if play_game == 'Y':
                game_on = True
            else:
                game_on = False

        while game_on:

            if turn == 'player 1':

                print('player 1 please choose a position')
                display_board(board)
                position = player_pos(board)
                place_marker(board, player1_marker, position)

                if win_check(board, player1_marker):
                    display_board(board)
                    print('player 1 has won')
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print("game is a tie")
                        break
                    else:
                        turn = 'player 2'
            else:

                print('player 2 please choose a position')
                display_board(board)
                position = player_pos(board)
                place_marker(board, player2_marker, position)

                if win_check(board, player2_marker):
                    display_board(board)
                    print('player 2 has won')
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print("game is a tie")
                        break
                    else:
                        turn = 'player 1'

        if not replay():
            break

tic_tac_toe()