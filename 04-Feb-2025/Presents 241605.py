# Problem: Presents - https://codeforces.com/problemset/problem/136/A

n = int(input())  
friends = list(map(int, input().split()))  
result = [0] * n  

for friend in range(1, n + 1):  
    receiver = friends[friend - 1]  
    result[receiver - 1] = friend  

print(*result)  
