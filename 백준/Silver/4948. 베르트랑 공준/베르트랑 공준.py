import math

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

m = list(range(2, 2*123456))
l = []

for j in m:
    if is_prime_number(j):
        l.append(j)
        
n = int(input())

while True:
    cnt = 0
    if n == 0:
        break
    for k in l:
        if n < k <= 2*n:
            cnt += 1
    print(cnt)
    n = int(input())