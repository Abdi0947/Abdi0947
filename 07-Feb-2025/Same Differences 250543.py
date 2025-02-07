# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D


def count_pairs(n, arr):
    freq = {}  
    count = 0

    for i in range(n):
        key = arr[i] - (i + 1) 
        if key in freq:
            count += freq[key]
        if key in freq:
            freq[key] += 1
        else:
            freq[key] = 1
    
    return count

t = int(input())

for _ in range(t):
    n = int(input())  
    arr = list(map(int, input().split()))  
    
    result = count_pairs(n, arr)
    
    print(result)
