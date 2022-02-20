def main(chart="         "):
    game_state = write_chart(chart)
    game_impossible = impossible(game_state)
    if game_impossible:
        return
    else:
        game_n_finished = game_not_finished(game_state)
        if game_n_finished:
            player_move(game_state)
        else:
            if x_wins(game_state):
                print('X wins')
            elif o_wins(game_state):
                print('O wins')
            else:
                draw()


def player_move(chart):
    new_chart = chart
    dict_of_chart = {11: new_chart[0], 12: new_chart[1], 13: new_chart[2],
                     21: new_chart[3], 22: new_chart[4], 23: new_chart[5],
                     31: new_chart[6], 32: new_chart[7], 33: new_chart[8]}

    while True:
        global x_turn
        move = input('Enter the coordinates: ').replace(" ", "")
        if not move.isdigit():
            print('You should enter numbers!')
        elif move not in ["11", "12", "13", "21", "22", "23", "31", "32", "33"] or len(move) != 2:
            print('Coordinates should be from 1 to 3!')
        elif dict_of_chart[int(move)] == "X" or dict_of_chart[int(move)] == "O":
            print('This cell is occupied! Choose another one!')
        else:
            move = int(move)
            break
    for key, value in dict_of_chart.items():
        if key == move:
            if x_turn:
                dict_of_chart[move] = "X"
                x_turn = False
            else:
                dict_of_chart[move] = "O"
                x_turn = True
    new_chart = "".join(dict_of_chart.values())
    main(new_chart)


def write_chart(chart="         "):
    go_on = True
    while go_on:
        if chart is None:
            symbols = input('Enter_cells: ')
            for symbol in symbols:
                if symbol not in ["X", "O", "_", " "] or len(symbols) != 9:
                    print('The input must be 9 characters in length and must only contain')
                    print('these symbols: X, O, _ or blank spaces. Try again.')
                    break
                else:
                    go_on = False
                    break
        else:
            symbols = chart
            break
    print('---------')
    print('|', symbols[0], symbols[1], symbols[2], '|')
    print('|', symbols[3], symbols[4], symbols[5], '|')
    print('|', symbols[6], symbols[7], symbols[8], '|')
    print('---------')
    return symbols


def impossible(symbols):
    game_state = symbols
    x_number = game_state.count('X')
    o_number = game_state.count('O')
    if x_wins(game_state) and o_wins(game_state):
        print('Impossible')
        return True
    elif abs(x_number - o_number) >= 2:
        print('Impossible')
        return True
    else:
        return False


def game_not_finished(symbols):
    game_state = symbols
    if (' ' in game_state or '_' in game_state) and (x_wins(game_state) is False and o_wins(game_state) is False):
        # print('Game not finished')
        return True
    else:
        return False


def draw():
    print('Draw')


def x_wins(symbols):
    game_state = symbols
    if game_state[0:3] == 'XXX' or game_state[3:6] == 'XXX' or game_state[6:] == 'XXX':  # HORIZONTAL
        return True
    elif game_state[0:7:3] == 'XXX' or game_state[1:8:3] == 'XXX' or game_state[2::3] == 'XXX':  # VERTICAL
        return True
    elif game_state[0::4] == 'XXX' or game_state[2:7:2] == 'XXX':  # DIAGONAIS
        return True
    else:
        return False


def o_wins(symbols):
    game_state = symbols
    if game_state[0:3] == 'OOO' or game_state[3:6] == 'OOO' or game_state[6:] == 'OOO':  # HORIZONTAL
        return True
    elif game_state[0:7:3] == 'OOO' or game_state[1:8:3] == 'OOO' or game_state[2::3] == 'OOO':  # VERTICAL
        return True
    elif game_state[0::4] == 'OOO' or game_state[2:7:2] == 'OOO':  # DIAGONAIS
        return True
    else:
        return False


if __name__ == '__main__':
    x_turn = True
    main()
