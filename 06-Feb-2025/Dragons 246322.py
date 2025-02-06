# Problem: Dragons - https://codeforces.com/problemset/problem/230/A

s, n = map(int, input().split())
dragons = [tuple(map(int, input().split())) for _ in range(n)]
def wins(s,dragons):
    dragons.sort()
    for x,y in dragons:
        if s>x:
            s+=y
        else:
            return "NO"
    return "YES"
print(wins(s,dragons))