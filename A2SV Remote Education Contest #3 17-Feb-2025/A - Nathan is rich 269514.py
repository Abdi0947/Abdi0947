# Problem: A - Nathan is rich - https://codeforces.com/gym/588094/problem/A

for i in range(int(input())):
    m=input()
    val=int(m)
    if val>=4:
        car=val//4
        remain=val%4
        if remain >=4:
            car+=remain//4
        elif remain >=2:
            car+=remain//2
    else:
        car=1
    print(car)
    
    
