import sys

n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline()
    c = 0
    sumC = 0
    for j in s:
        if j == "O":
            c += 1
        else:
            c = 0
        sumC += c
    print(sumC)