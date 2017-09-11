import copy
# sudoku = [[1, 2, 4, 0, 8, 3, 9, 5, 7],
#           [0, 0, 3, 6, 0, 0, 0, 0, 0],
#           [0, 7, 0, 0, 9, 0, 2, 0, 0],
#           [0, 5, 0, 0, 0, 7, 0, 0, 0],
#           [0, 0, 0, 8, 4, 5, 7, 0, 0],
#           [0, 0, 0, 1, 0, 0, 0, 3, 0],
#           [0, 0, 1, 0, 0, 0, 0, 6, 8],
#           [0, 0, 0, 5, 0, 0, 0, 1, 0],
#           [0, 9, 0, 0, 0, 0, 4, 0, 0]]
# x=4
# y=4
sudoku = [[2, 0, 0, 0, 0, 6, 0, 7, 0], [7, 0, 4, 0, 2, 9, 0, 6, 1], [0, 6, 0, 0, 0, 4, 9, 0, 0], [8, 0, 7, 0, 0, 0, 0, 0, 6], [0, 1, 0, 0, 3, 0, 0, 5, 0], [5, 0, 0, 0, 0, 0, 2, 9, 0], [0, 0, 0, 0, 0, 0, 6, 4, 0], [0, 5, 0, 6, 0, 1, 7, 0, 8], [0, 8, 6, 4, 0, 0, 0, 0, 0]]
sudoku = [[1, 0, 4, 5, 7, 3, 2, 8, 9], [2, 3, 7, 1, 8, 9, 5, 6, 4], [9, 8, 5, 6, 2, 4, 1, 3, 7], [5, 9, 6, 4, 3, 2, 8, 7, 1], [4, 7, 8, 9, 5, 1, 3, 2, 6], [3, 1, 2, 8, 6, 7, 9, 4, 5], [6, 2, 1, 7, 9, 8, 4, 5, 3], [8, 5, 9, 3, 4, 6, 7, 1, 2], [7, 4, 3, 2, 1, 5, 6, 9, 8]]

class Solution(object):
    def __init__(self, _sudoku):
        self.sudoku = copy.deepcopy(_sudoku)
        self.count = 0
        self.cal()

    # 检查num是否能填进(x,y)里
    def check(self, x, y, num):
        if num in self.sudoku[y]:  # 行中是否有相同元素
            return False
        elif num in [i[x] for i in self.sudoku]:  # 列中是否有相元素
            return False
        elif num in [j for i in self.sudoku[y - y % 3:(y - y % 3) + 3] for j in i[x - x % 3:(x - x % 3) + 3]]:  # 小格中是否有相同元素
            return False
        else:
            # print(self.sudoku[y])
            return True

    # 找到下一个需要填的数，返回坐标；如果已经填完，返回（-1，-1）
    def get_next(self, x, y):
        for i in range(x+1, 9):
            if self.sudoku[y][i] == 0:
                return i, y
        for i in range(y+1, 9):
            for j in range(9):
                if self.sudoku[i][j] == 0:
                    return j, i
        return -1, -1

    # 解出点(x,y)的结果，如果解出，则解(next_x,next_y)的结果；解不出或(next_x,next_y)无法顺利填完，则返回False
    def solve(self, x, y):
        # if self.count > 1:
        #     return
        next_x, next_y = self.get_next(x, y)
        # print(next_x,next_y)
        for i in range(1, 10):  # 将1-9尝试填入当前的空格
            if self.check(x, y, i):  # 如果可以填入，则填入
                self.sudoku[y][x] = i
                # print(self.sudoku)
                if next_x == -1:  # 如果已经填完，返回True
                    # print(self.sudoku)
                    self.count = self.count + 1
                    self.sudoku[y][x] = 0
                else:
                    self.solve(next_x, next_y)  # 如果未填完，填下一个，如果后续节点均顺利填完（返回True），则也返回True
        self.sudoku[y][x] = 0  # 遍历了所有结果，都无法填入，则将当前结点改回0，返回False

    # 返回第一个节点
    def get_first(self):
        return self.get_next(-1, 0)

    def cal(self):
        first_x, first_y = self.get_first()
        self.solve(first_x, first_y)

if __name__ == "__main__":
    sudoku = [
        [8,0,0,0,0,0,0,0,0],
        [0,0,3,6,0,0,0,0,0],
        [0,7,0,0,9,0,2,0,0],
        [0,5,0,0,0,7,0,0,0],
        [0,0,0,0,4,5,0,0,0],
        [0,0,0,1,0,0,0,3,0],
        [0,0,1,0,0,0,0,6,8],
        [0,0,8,5,0,0,0,1,0],
        [0,9,0,0,0,0,4,0,0]
    ]
    s = Solution(sudoku)
    # print(s.sudoku)
    print(s.count)
