import sys
from math import factorial as f

n = f(int(sys.stdin.readline()))
n = str(n)
cnt = 0
for i in reversed(n):
    if i == '0':
        cnt += 1
    else:
        break

print(cnt)