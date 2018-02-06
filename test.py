from createSudokuProblem import Problem

problem = Problem()
sudokuLst = problem.create()

for i in sudokuLst:
    for j in i:
        print(j)
    print('-------------------------------')


# print(creatSudokuProblem.create())
# print(creatSudokuProblem.create())
# i = [[0, 4, 0, 0, 1, 0, 0, 7, 0],
# [5, 0, 0, 8, 0, 0, 0, 9, 0],
# [7, 0, 0, 0, 0, 0, 0, 0, 5],
# [0, 0, 0, 0, 0, 0, 0, 2, 8],
# [0, 0, 9, 1, 0, 8, 0, 0, 6],
# [0, 0, 6, 9, 5, 0, 3, 1, 0],
# [6, 0, 7, 5, 9, 4, 0, 0, 1],
# [1, 2, 5, 7, 6, 0, 0, 0, 0],
# [0, 0, 0, 2, 0, 0, 0, 0, 0]]
# count = 0
# for k in i:
#     for x in k:
#         if x != 0:
#             count += 1
# print(count)