# here we go

board = list(range(1, 10))


def print_board(b):
    j = 1
    for i in board:
        end = ''
        if j % 3 == 0:
            end = '\n\n'
        if i == 'o':
            pass
        elif i == 'x':
            pass
        else:
            print(f'[{i}]', end=end)
        j += 1


print_board(board)
