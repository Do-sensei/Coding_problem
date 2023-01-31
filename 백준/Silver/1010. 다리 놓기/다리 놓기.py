import sys
from math import factorial as f
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(f(b) // (f(a) * f(b - a)))