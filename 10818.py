import sys

N = int(sys.stdin.readline())

m = list(map(int, sys.stdin.readline().split()))
print(min(m), max(m))