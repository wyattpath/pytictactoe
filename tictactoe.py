def print_game(matrix):
    print("---------")
    for count in range(3):
        print("| " + matrix[(count * 3)] + " " + matrix[(count * 3) + 1] + " " + matrix[(count * 3) + 2] + " |")
    print("---------")


def add_move(matrix, entries):
    entry = input('Enter the coordinates: ').split(' ')
    if not len(entry) == 2:
        print('You should enter 2 numbers!')
        return add_move(matrix, entries)
    if not entry[0].isnumeric() or not entry[1].isnumeric():
        print('You should enter numbers!')
        return add_move(matrix, entries)
    if int(entry[0]) not in range(1, 4) or int(entry[1]) not in range(1, 4):
        print('Coordinates should be from 1 to 3!')
        return add_move(matrix, entries)
    row = 3 - int(entry[1])
    col = int(entry[0]) - 1
    if matrix[row][col] not in ['X', 'O']:
        matrix[row][col] = 'O' if entries.count('X') > entries.count('O') else 'X'
        return matrix
    print('This cell is occupied! Choose another one!')
    return add_move(matrix, entries)


def game_loop(entries):
    global game_over
    print_game(entries)
    if game_over:
        return
    matrix_horizontal = [
        [entries[0], entries[1], entries[2]],
        [entries[3], entries[4], entries[5]],
        [entries[6], entries[7], entries[8]]
    ]
    matrix_vertical = [
        [entries[0], entries[3], entries[6]],
        [entries[1], entries[4], entries[7]],
        [entries[2], entries[5], entries[8]]
    ]
    matrix_diagonal = [
        [entries[0], entries[4], entries[8]],
        [entries[2], entries[4], entries[6]]
    ]
    all_results = [matrix_horizontal, matrix_vertical, matrix_diagonal]
    game_results = [entry for entry in all_results for entry in entry]

    stage_message = ''
    if (entries.count("X") >= entries.count("O") + 2) or (entries.count("O") >= entries.count("X") + 2) or (
            ['O', 'O', 'O'] in game_results and ['X', 'X', 'X'] in game_results):
        stage_message = 'Impossible'
        game_over = True
    elif (entries.count("X") + entries.count("O") < 9) and (
            ['O', 'O', 'O'] not in game_results and ['X', 'X', 'X'] not in game_results):
        # Game not finished
        matrix_horizontal = add_move(matrix_horizontal, entries)
    elif ['O', 'O', 'O'] in game_results:
        stage_message = 'O wins'
        game_over = True
    elif ['X', 'X', 'X'] in game_results:
        stage_message = 'X wins'
        game_over = True
    else:
        stage_message = 'Draw'
        game_over = True
    if game_over:
        print(stage_message)
    else:
        game_loop([entry for row in matrix_horizontal for entry in row])


game_over = False
game_loop(list('         '))
