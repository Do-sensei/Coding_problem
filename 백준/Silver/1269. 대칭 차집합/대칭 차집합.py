import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr_a = set(map(int, input().split()))
arr_b = set(map(int, input().split()))

print(len(arr_a - arr_b) + len(arr_b - arr_a))