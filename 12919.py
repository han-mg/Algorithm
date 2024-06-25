import sys

s = str(sys.stdin.readline().strip())
t = str(sys.stdin.readline().strip())

def change(t):
    if s == t:
        return 1
    if len(t) <= len(s):
        return 0
    if t[0] == 'B':
        r = t[::-1]
        e = r[:-1]
        if change(e):
            return 1
    if t[-1] == 'A':
        c = t[:-1]
        if change(c):
            return 1
    return 0

print(change(t))