def game(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print('This position is accupado! Choose another.')
            return game_map, False
        if not just_display:
            game_map[row][column] = player
        print('   ' + '  '.join([str(i) for i in range(len(game_map))]))
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError as e:
        print('Error: Make sure you input row/column as 0 1 or 2?', e)
        return game_map, False
    except Exception as e:
        print('Something went very wrong!', e)
        return game_map, False


def win(current_game):
    def all_same(list):
        if list.count(list[0]) == len(list) and list[0] != 0:
            return True
        else:
            return False
    #Horizontal
    for row in game_board:
        if all_same(row):
            print(f'Player {row[0]} is the winner horizontally! (---)')
            return True

    #Vertical
    for i in range(len(game_board)):
        vert = []
        for row in game_board:
            vert.append(row[i])
    if all_same(vert):
                print(f'Player {vert[0]} is the winner vertically! (|)')
                return True

    #Diagonal
    diags = []
    for i in range(len(game_board)):
        diags.append(game_board[i][i])
    if all_same(diags):
        print(f'Player {diags[0]} is the winner diagonally! (\\)')
        return True

    diags = [] 
    for col, row in enumerate(reversed(range(len(game_board)))):
        diags.append(game_board[row][col])
    if all_same(diags):
        print(f'Player {diags[0]} is the winner diagonally! (/)')
        return True
    #print('Ops..It is a draw!')
    return False

def draw(list):
    draw = True
    for line in range(len(list)):
        if list.count(0) >= 0:
            draw = False
    if draw:
        print('Ops...It is a draw!')
        return True
    return False

play = True
player = [1, 2]
while play:
    game_size = int(input('What size game of tic-tac-toe? '))
    game_board = [[0 for i in range(game_size)]for i in range(game_size)]
    game(game_board,just_display=True)
    game_won = False
    while not game_won:
        current_player = player[0]
        print(f'Current playet: {current_player}')
        played = False
        while not played:
            col_choice = int(input('What column do you want to play? (0, 1, 2): '))
            row_choice = int(input('What row do you want to play? (0, 1, 2): '))
            game_board, played = game(game_board, current_player, row_choice, col_choice)
        player = player[::-1]
        if win(game_board) or draw(game_board):
            game_won = True
            again = input('The game is over! Would you like to play again? (y/n): ')
            if again.lower() == 'y':
                print('Restarting...')
            if again.lower() == 'n':
                print('Bye...')
                play = False
            else:
                print('Not a valid answer, bye......')
                play = False
