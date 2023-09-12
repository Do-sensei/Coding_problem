import sys
input = sys.stdin.readline

n = int(input())

start = n - 9 * len(str(n))
if start < 1:
    start = 1

for i in range(start, n):
    if i + sum(map(int, str(i))) == n:
        print(i)
        break
else: 
    print(0)
