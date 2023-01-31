from math import factorial as f
import sys

n, m = map(int, sys.stdin.readline().split())
print(f(n) // (f(m) * f(n - m)))