# Problem: Python power-mod-power - https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true

a = int(input()) 
b = int(input())  
m = int(input())  

result = pow(a, b)  
reminder = result % m  
print(result)  
print(reminder)  