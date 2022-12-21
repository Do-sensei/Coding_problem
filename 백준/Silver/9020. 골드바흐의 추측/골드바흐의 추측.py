import math

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

n = int(input())
for _ in range(n):
    m = int(input())
    
    a, b = m//2, m//2
    while a > 0:
        if is_prime_number(a) and is_prime_number(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1