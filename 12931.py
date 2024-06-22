n = int(input())
a = list(map(int, input().split()))

cnt = 0

while True:
    for i in range(n):
        if a[i] % 2 == 1:
            a[i] -= 1
            cnt += 1
    if sum(a) == 0:
        break
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] /= 2
    cnt += 1
print(cnt)