# Problem: Runner up score - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))  
    fmax = max(arr)  
    arr = [x for x in arr if x != fmax] 
    smax = max(arr)  
    print(smax)