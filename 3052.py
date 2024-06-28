import sys

a = []
for i in range(10):
    n = int(sys.stdin.readline()) % 42
    if n not in a:
        a.append(n)

print(len(a))