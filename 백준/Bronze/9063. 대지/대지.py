import sys
input = sys.stdin.readline

n = int(input())

def earth(n):
    X, Y = [], []

    for _ in range(n):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    X_dist = max(X) - min(X)
    Y_dist = max(Y) - min(Y)

    print(X_dist * Y_dist)

earth(n)