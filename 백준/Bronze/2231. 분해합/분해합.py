import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    if i + sum(map(int, str(i))) == n:
        print(i)
        break
    else:
        if i == n:
            print(0)