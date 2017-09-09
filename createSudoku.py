import random

class Sudoku(object):
    def __init__(self):
        self.set1 = set(range(1, 10))
        self.fuck = 0

    def do(self, x, y):
        self.fuck = self.fuck + 1
        # print(x,y)
        set2 = set(self.sudoku[y][:x]) | {i[x] for i in self.sudoku[:y]} | {j for i in self.sudoku[y - y % 3:(y - y % 3) + 3] for j in i[x - x % 3:(x - x % 3) + 3]}
        set3 = self.set1 - set2
        while len(set3) > 0:
            self.sudoku[y][x] = random.choice(list(set3))
            # print((x + 1) % 9, y + x // 9)
            if (x == 8 and y == 8) or self.do((x + 1) % 9, y + (x + 1) // 9):
                # print(sudoku)
                return True
            else:
                # print(sudoku)
                set3 = set3 - {self.sudoku[y][x]}
                # print(set3)
        self.sudoku[y][x] = 0
        return False

    def create(self):
        self.sudoku = [[0 for i in range(9)] for i in range(9)]
        self.do(0, 0)
        return self.sudoku


if __name__ == "__main__":
    A = Sudoku()
    for i in range(1000):
        A.create()
        print(i)
    print(A.fuck/1000)
    # create()
    # print(sudoku)