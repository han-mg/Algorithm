import sys
n = map(int, sys.stdin.readline().split())
result = 0
for i in n:
    result += i * i
print(result % 10)