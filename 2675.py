import sys

T = int(sys.stdin.readline())

for i in range(T):
    R, S = sys.stdin.readline().split()
    for i in range(len(S)):
        print(int(R) * S[i], end='')
    print()