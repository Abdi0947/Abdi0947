# Problem: D - Mugisho and Rufeyda - https://codeforces.com/gym/586622/problem/D

n, t = [int(i) for i in input().split()]

start = int('1' + '0' *(n-1) )
end = int('1'+'0' * n)

ans = -1
for i in range(start, end ):
    if i % t == 0:
        ans = i
        break
    
print(ans)
