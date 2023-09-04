import sys
input = sys.stdin.readline

a = 0
b = 0
for i in range(2):
    if i == 0:
        a = int(input())
    else:
        b = int(input())

print(a*b)