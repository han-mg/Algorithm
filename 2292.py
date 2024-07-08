import sys

N = int(sys.stdin.readline())
b = 1
for i in range(N):
   b += i * 6
   if N <= b:
      print(i+1)
      break