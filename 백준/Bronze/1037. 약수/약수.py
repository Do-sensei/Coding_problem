import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
print(arr[0]* arr[-1])    