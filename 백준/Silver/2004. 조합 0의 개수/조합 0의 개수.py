import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def cnt_num(n, num):
    cnt = 0
    while n:
        n //= num
        cnt += n
    return cnt

cnt_5 = cnt_num(n, 5) - cnt_num(m, 5) - cnt_num(n - m, 5)
cnt_2 = cnt_num(n, 2) - cnt_num(m, 2) - cnt_num(n - m, 2)

print(min(cnt_5, cnt_2))

