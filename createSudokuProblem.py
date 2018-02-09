import calSudoku
import createSudoku
import random
import copy


class Problem(object):
    def __init__(self):
        self.sudoku = []
        self.lst = []
        self.blockNum = 45

    def dig(self, count):
        # print(count)
        if count == self.blockNum:
            return True
        templst = copy.copy(self.lst)
        while len(self.lst):
            # print(lst)
            num = random.randint(0, len(self.lst) - 1)
            k = self.lst.pop(num)
            x = k % 9
            y = k // 9
            temp = self.sudoku[y][x]
            self.sudoku[y][x] = 0
            cal = calSudoku.Solution(self.sudoku)
            if cal.count == 1:  # 如果有且仅有一个解，挖下一个
                if self.dig(count+1):
                    return True
            self.sudoku[y][x] = temp
            # lst.insert(num, k)
        self.lst = templst
        return False

    def create(self):
        self.lst = [i for i in range(81)]
        cs = createSudoku.Sudoku()
        self.sudoku = cs.create()
        ts = copy.deepcopy(self.sudoku)
        self.dig(0)
        return self.sudoku, ts

if  __name__ == "__main__":
    A = Problem()
    print(A.create())
    print(A.create())
