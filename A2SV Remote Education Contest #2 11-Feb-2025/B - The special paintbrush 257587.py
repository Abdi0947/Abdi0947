# Problem: B - The special paintbrush - https://codeforces.com/gym/586622/problem/B

def min(n, s):
    first = s.find('B')
    last = s.rfind('B')
    
    return last - first + 1
t = int(input())

for _ in range(t):
    n = int(input())  
    s = input().strip()  
    print(min(n,s))


