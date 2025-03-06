# Problem: C - Happy Partitioning - https://codeforces.com/gym/590201/problem/C

for case in range(int(input())):
    n = int(input())  
    a = input() 
    suf_cnt = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suf_cnt[i] = suf_cnt[i + 1] + (a[i] == '1')

    pref_cnt = 0  
    opt_ans = -1  
    opt_dist = n * 2 
    threshold = (n + 1) // 2  
    for i in range(n + 1):
        if pref_cnt >= (i + 1) // 2 and suf_cnt[i] >= (n - i + 1) // 2 and abs(n - 2 * i) < opt_dist:
            opt_dist = abs(n - 2 * i)
            opt_ans = i
        
        if i != n:
            pref_cnt += (a[i] == '0')
    print(opt_ans)
