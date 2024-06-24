import sys

T = int(sys.stdin.readline())

for i in range(T):
    stack = []
    s = input()
    for j in s:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")