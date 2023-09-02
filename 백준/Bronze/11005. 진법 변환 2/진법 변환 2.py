import sys
input = sys.stdin.readline

N, B = map(int, input().split())

def convert(num, base):
    T = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    q, r = divmod(num, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
    
print(convert(N, B))