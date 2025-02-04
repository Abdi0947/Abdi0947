# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

import math

# Input the dimensions of the rectangle and the flagstone size
n, m, a = map(int, input().split())

# Calculate the number of flagstones needed
flagstones_x = math.ceil(n / a)
flagstones_y = math.ceil(m / a)

# Total flagstones
total_flagstones = flagstones_x * flagstones_y

print(total_flagstones)
