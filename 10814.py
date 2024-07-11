import sys

N = int(sys.stdin.readline())

m = []

for i in range(N):
    a, n = map(str, sys.stdin.readline().split())
    a = int(a)
    m.append((a, n))

m.sort(key=lambda x: x[0])

for i in m:
    print(i[0], i[1])
