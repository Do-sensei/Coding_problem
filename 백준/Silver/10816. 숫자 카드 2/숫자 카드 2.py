from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
arr_1 = list(map(int, input().split()))
arr_1_dic = Counter(arr_1)

m = int(input())
arr_2 = list(map(int, input().split()))

for i in arr_2:
    print(arr_1_dic.get(i, 0), end=' ')