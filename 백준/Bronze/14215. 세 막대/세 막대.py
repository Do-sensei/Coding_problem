import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

length = sorted([a, b, c])

if length[0] + length[1] <= length[2]:
    print((length[0]+length[1])*2-1)
else:
    print(sum(length))