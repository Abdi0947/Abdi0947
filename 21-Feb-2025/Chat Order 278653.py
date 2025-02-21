# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

n = int(input())
nums = [input().strip() for _ in range(n)] 

seen = set() 
arr = []  

for num in reversed(nums):
    if num not in seen:
        seen.add(num)
        arr.append(num)
print("\n".join(arr))
