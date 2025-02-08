# Problem: Python Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    n= int(input())
    arr=[]
    for i in range(n):
        command=input().split()
        
        if command[0]=='append':
            arr.append(int(command[1]))
        elif command[0]=='insert':
            arr.insert(int(command[1]),int(command[2]))
        elif command[0]=='remove':
            arr.remove(int(command[1]))
        elif command[0]=='sort':
            arr.sort()
        elif command[0]=='pop':
            arr.pop()
        elif command[0]=='reverse':
            arr.reverse()
        else:
           print(arr)
