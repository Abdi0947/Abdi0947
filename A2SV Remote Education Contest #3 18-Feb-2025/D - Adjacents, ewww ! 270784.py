# Problem: D - Adjacents, ewww ! - https://codeforces.com/gym/588094/problem/D

def solve():
    n = int(input())

    if n == 1:
        print(1)
        return
    elif n == 2:
        print(-1)
        return

    matrix = [[0] * n for _ in range(n)]
    num = 1
    
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:  
                matrix[i][j] = num
                num += 1
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:  
                matrix[i][j] = num
                num += 1

    for row in matrix:
        print(*row)


t = int(input())
for _ in range(t):
    solve()