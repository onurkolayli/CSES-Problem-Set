# Task -> https://cses.fi/problemset/task/1083/
# About Me -> https://github.com/onurkolayli

n = int(input())
s = 0
x = [int(x) for x in input().split()]

for i in range(len(x)):
    s += x[i]

ans = int((n * (n + 1)) / 2 - s)
print(ans)