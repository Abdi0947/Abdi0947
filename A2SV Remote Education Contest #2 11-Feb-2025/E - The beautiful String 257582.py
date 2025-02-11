# Problem: E - The beautiful String - https://codeforces.com/gym/586622/problem/E

import sys

def check_1100(buf, i, n):
    """Check if '1100' occurs starting at index i"""
    return i + 3 < n and buf[i] == '1' and buf[i + 1] == '1' and buf[i + 2] == '0' and buf[i + 3] == '0'

def solve():
    buf = list(sys.stdin.readline().strip())
    n = len(buf)
    
    # Step 1: Precompute the initial count of "1100"
    count = sum(1 for i in range(n - 3) if check_1100(buf, i, n))

    q = int(sys.stdin.readline().strip())
    for _ in range(q):
        i, v = map(int, sys.stdin.readline().split())
        i -= 1  # Convert to 0-based index

        if buf[i] == str(v):  # If no actual change, just print current result
            print("YES" if count > 0 else "NO")
            continue

        # Step 2: Decrease count for affected indices (i-3 to i)
        for j in range(max(0, i - 3), min(n - 3, i + 1)):
            if check_1100(buf, j, n):
                count -= 1  # Remove the old occurrence

        # Step 3: Apply the change
        buf[i] = str(v)

        # Step 4: Re-check affected region for new "1100"
        for j in range(max(0, i - 3), min(n - 3, i + 1)):
            if check_1100(buf, j, n):
                count += 1  # Add new occurrence

        # Step 5: Print the result
        print("YES" if count > 0 else "NO")

t = int(sys.stdin.readline().strip())
for _ in range(t):
    solve()
