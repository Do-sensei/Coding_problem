import sys
from math import sqrt
from math import gcd

n = int(sys.stdin.readline())
n_arr = sorted([int(sys.stdin.readline()) for _ in range(n)])
diff = []
answer = []

for i in range(n-1):
    diff.append(n_arr[i+1] - n_arr[i])
    
n_gcd = gcd(*diff)
answer.append(n_gcd)
for j in range(2, int(sqrt(n_gcd))+1):
    if n_gcd % j == 0:
        answer.append(j)
        answer.append(n_gcd//j)

answer = set(answer)
print(*sorted(answer))