# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

matrix = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row, col = i, j
            break
row_moves = abs(row - 2)  
col_moves = abs(col - 2) 

print(row_moves + col_moves)