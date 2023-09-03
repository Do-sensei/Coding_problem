import sys
input = sys.stdin.readline

N = int(input())

def get_points(n):
    if n == 0:
        return 2
    else:
        return get_points(n-1) + 2**(n-1)
    
print(get_points(N)**2)