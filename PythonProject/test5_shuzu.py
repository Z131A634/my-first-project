 # 列表初始化

matrix = []

rows = 3
cols = 4

for i in range(rows):
     matrix.append([i * 3 + j for j in range(cols)])

rows = 3
cols = 4
# 同样初始化一个 3 行 4 列的二维列表，元素初始值为 0
matrix = [[0 for j in range(cols)] for i in range(rows)]
print(matrix)