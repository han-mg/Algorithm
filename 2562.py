import sys
n = []

for _ in range(9):
    i = int(sys.stdin.readline())
    n.append(i)

print(max(n))
print(n.index(max(n))+1)