import calSudoku
import createSudoku
import random
import copy

global s
global lst
blockNum = 45
# count = 0
# for i in range(10):
#     num = random.randint(0, len(lst) - 1)
#     num = lst.pop(num)
#     x = num % 9
#     y = num // 9
#     count += 1
#     s[y][x] = 0


def dig(count):
    # print(count)
    global lst
    global s
    if count == blockNum:
        return True
    templst = copy.copy(lst)
    while len(lst):
        # print(lst)
        num = random.randint(0, len(lst) - 1)
        k = lst.pop(num)
        x = k % 9
        y = k // 9
        temp = s[y][x]
        s[y][x] = 0
        cal = calSudoku.Solution(s)
        if cal.count == 1:
            if dig(count+1):
                return True

        s[y][x] = temp
        # lst.insert(num, k)
    lst = templst
    return False

def create():
    global lst
    global s
    lst = [i for i in range(81)]
    cs = createSudoku.Sudoku()
    s = cs.create()
    ts = copy.deepcopy(s)
    dig(0)
    return s, ts

if  __name__ == "__main__":

    print(create())
    print(create())
