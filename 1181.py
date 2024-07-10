import sys

N = int(sys.stdin.readline())
words = []
for i in range(N):
    words.append(sys.stdin.readline().strip())

set_words = set(words)
lis = list(set_words)
lis.sort()
lis.sort(key=len)

for i in lis:
    print(i)