# Task -> https://cses.fi/problemset/task/1069
# About Me -> https://github.com/onurkolayli

n = input()
ans = c = 0
l = 'A'
for i in n:
    if i == l:
        c += 1
        ans = max(ans, c)
    else:
        l = i
        c = 1
print(ans)