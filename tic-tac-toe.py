# here we go

board = list(range(1, 10))
winner = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
moves = ((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2))


def print_board():
    j = 1
    for i in board:
        end = ''
        if j % 3 == 0:
            end = '\n\n'
        if i == 'o':
            print(f'[{i}]', end=end)
        elif i == 'x':
            print(f'[{i}]', end=end)
        else:
            print(f'[{i}]', end=end)
        j += 1


def make_move(b, pl, mv, undo=False):
    if can_move(b, mv):
        b[mv - 1] = pl
        win = is_winner(b, pl)
        if undo:
            b[mv - 1] = mv
        return True, win
    return True, True  #moved, won


def can_move(b, mv):
    if mv in range(1, 10) and isinstance(b[mv - 1], int):
        return True
    else:
        return False


def is_winner(b, pl):
    for t in winner:  #searches 8 lil tuples
        win = True
        for i in t:  #searches 3 nums inside lil tuples
            if b[i] != pl:
                win = False
                break
        if win:
            break
    return win


def computer_mv():
    mv = -1  #do not move
    # can you win?
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            mv = i
            break
    # would pl win?
    for j in range(1, 10):
        if make_move(board, player, j, True)[1]:
            mv = j
            break
    # if neither, prioritize your mv
    if mv == -1:
        for t in moves:
            for i in t:
                if can_move(board, i):
                    mv = i
                    break
    return make_move(board, computer, mv)


def empty_space():
    return board.count('o') + board.count('x') != 9


computer, player = 'o', 'x'
print('computer: o\nplayer: x')
while empty_space():
    print_board()
    move = int(input('make your move: '))
    moved, won = make_move(board, player, move)
    if not moved:
        print('invalid num! try again')
        continue
    if won:
        print('you won!')
        break
    # elif computer_mv()[1]:
    #     print('you lose!!')
    #     break

print_board()

# check make move func and change (moved-won) part in last loop!
