# Task -> https://cses.fi/problemset/task/1094/
# About Me -> https://github.com/onurkolayli

n = int(input())
x = [int(x) for x in input().split()]
ans = m = 0
for i in range(n):
    m = max(x[i], m)
    ans += m - x[i]
print(ans)