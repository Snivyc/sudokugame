import random

set1 = set(range(1, 10))


global sudoku


def do(x, y):
    global sudoku
    # print(x,y)
    set2 = set(sudoku[y]) | {i[x] for i in sudoku} | {j for i in sudoku[y - y % 3:(y - y % 3) + 3] for j in i[x - x % 3:(x - x % 3) + 3]}
    set3 = set1 - set2
    while len(set3) > 0:
        sudoku[y][x] = random.choice(list(set3))
        # print((x + 1) % 9, y + x // 9)
        if (x == 8 and y == 8) or do((x + 1) % 9, y + (x + 1) // 9):
            # print(sudoku)
            return True
        else:
            # print(sudoku)
            set3 = set3 - {sudoku[y][x]}

            # print(set3)
    sudoku[y][x] = 0
    return False


def create():
    global sudoku
    sudoku = [[0 for i in range(9)] for i in range(9)]
    do(0, 0)
    return sudoku


if __name__ == "__main__":
    create()
    print(sudoku)
    create()
    print(sudoku)