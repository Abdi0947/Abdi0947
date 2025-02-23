# Problem: D - Great Photographer - https://codeforces.com/gym/590201/problem/D

def bob_m(answer, m):
    L = max(ans[0] for ans in answer)
    H = min(ans[1] for ans in answer)

    if L > H:
        return -1
    elif m < L:
        return L - m
    elif m > H:
        return m - H
    else:
        return 0

k, m = input().split()
k = int(k)
m = int(m)
answer = []
for _ in range(k):
    a, b = input().split()
    answer.append((min(int(a), int(b)), max(int(a), int(b))))
res = bob_m(answer, m)
print(res)