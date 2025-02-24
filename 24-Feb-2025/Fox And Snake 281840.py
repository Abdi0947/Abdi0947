# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

n,m=map(int,(input().split()))
if n%2 ==0:
  print("enter n odd number")
  n,m=map(int(input().split()))
row=1
isLast=True
for i in range(n):
  if i%2==0:
       print("#"*m)
  else:
    if isLast:
        print("."*(m-1)+"#")
        isLast=False
    else:
        print("#"+"."*(m-1))
        isLast=True
       
       

  

  