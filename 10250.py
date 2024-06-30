import sys

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    f = N % H
    r = (N // H) + 1
    if f == 0:
        f = H
        r -= 1
    print(f * 100 + r)
