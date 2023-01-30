import sys
from fractions import Fraction
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))

for i in range(1, n):
    if Fraction(m[0], m[i]).denominator == 1:
        print(Fraction(m[0], m[i]), "/1", sep="")
    else:
        print(Fraction(m[0], m[i]))