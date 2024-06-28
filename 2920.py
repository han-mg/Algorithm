import sys

n = list(map(int, sys.stdin.readline().strip().split()))

if n == sorted(n):
    print('ascending')
elif n == sorted(n, reverse=True):
    print('descending')
else:
    print('mixed')