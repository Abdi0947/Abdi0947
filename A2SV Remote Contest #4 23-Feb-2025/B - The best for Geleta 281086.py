# Problem: B - The best for Geleta - https://codeforces.com/gym/590201/problem/B

def process_test_cases():
    n = int(input())  
    for _ in range(n):
        
        n, m = map(int, input().split())
 
        a = list(map(int, input().split()))
    
        max_a = max(a)
        ans = []
        
        for _ in range(m):
            op, l, r = input().split()
            l = int(l)
            r = int(r)
            if op == '+':
                if l <= max_a <= r:
                    max_a += 1
            elif op == '-':
                if l <= max_a <= r:
                    max_a -= 1
            ans.append(str(max_a))
        print(' '.join(ans))
process_test_cases()