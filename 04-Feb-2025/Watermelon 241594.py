# Problem: Watermelon - https://codeforces.com/problemset/problem/4/A

w = int(input())  # Input the weight of the watermelon

# Check if the weight is even and greater than 2
if w > 2 and w % 2 == 0:
    print("YES")
else:
    print("NO")
