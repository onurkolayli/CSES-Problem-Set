# Task -> https://cses.fi/problemset/task/1070/
# About Me -> https://github.com/onurkolayli

n = int(input())
if(n == 1):
    print(1)    
if(n==2 or n==3):
    print("NO SOLUTION")
if(n%2==0):
    for i in range(2, n+1, 2):
        print(i, end=" ")
    for j in range(1, n+1, 2):
        print(j, end=" ")
else:
    for i in range(n-1, 0, -2):
        print(i, end=" ")
    for j in range(n, 0, -2):
        print(j, end=" ")