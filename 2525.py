H, M = map(int, input().split())
C = int(input())

H += C // 60
M += C % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24
print(H, M)