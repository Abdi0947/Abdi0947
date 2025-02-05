# Problem: List Comprehensions - https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

x = int(input())  
y = int(input())  
z = int(input())  
n = int(input())  

# List comprehension to generate the 3D coordinates
result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]

# Print the result
print(result)
