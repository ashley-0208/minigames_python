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
        if i == 'o' or i == 'x':
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
    return False, False   # if move is invalid, return False for both


def can_move(b, mv):
    if mv in range(1, 10) and isinstance(b[mv - 1], int):
        return True
    return False


def is_winner(b, pl):
    for t in winner:
        if all(b[i] == pl for i in t):
            return True
    return False


def computer_mv():
    # اول: بررسی کنید آیا کامپیوتر می‌تواند برنده شود
    for p in range(1, 10):
        if can_move(board, p):
            _, win = make_move(board, computer, p, undo=True)  # شبیه‌سازی حرکت
            if win:  # اگر این حرکت باعث برنده شدن کامپیوتر شود
                return make_move(board, computer, p)  # حرکت واقعی را انجام دهید
#  پارامتر - در واقع به مقدار can move در تابع make move برمیگرده واینجا فقط win رو بررسی میکنه.
    # دوم: بررسی کنید آیا بازیکن می‌تواند برنده شود و جلوی آن را بگیرید
    for p in range(1, 10):
        if can_move(board, p):
            _, win = make_move(board, player, p, undo=True)  # شبیه‌سازی حرکت بازیکن
            if win:  # اگر این حرکت باعث برنده شدن بازیکن شود
                return make_move(board, computer, p)  # جلوی آن را بگیرید

    # سوم: اگر هیچ کدام از موارد بالا نبود، یک حرکت تصادفی انجام دهید
    for p in range(1, 10):
        if can_move(board, p):
            return make_move(board, computer, p)  # حرکت تصادفی

    # اگر هیچ حرکتی ممکن نبود، False برگردانید
    return False, False


def empty_space():
    return any(isinstance(cell, int) for cell in board)


computer, player = 'o', 'x'
print('computer: *\nplayer: x')

while empty_space():
    # نوبت بازیکن
    print_board()
    move = int(input('make your move: '))
    move_valid, player_won = make_move(board, player, move)

    if not move_valid:
        print('invalid move!')
        continue

    if player_won:
        print_board()
        print('You win!')
        break

    # نوبت کامپیوتر
    computer_move_valid, computer_won = computer_mv()

    if computer_won:
        print_board()
        print('You lose!')
        break

    # بررسی مساوی شدن بازی
    if not empty_space():
        print_board()
        print("It's a tie!")
        break


print_board()
