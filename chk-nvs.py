# myTuple = ("John", "Peter", "Vicky")
#
# x = "-".join(myTuple)
#
# print(x)

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


display_board()
