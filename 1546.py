import sys

N = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
M = max(s)

for i in range(N):
    s[i] = s[i] / M * 100
print(sum(s)/N)
