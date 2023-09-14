import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()

sys.stdout.write('\n'.join(map(str, a)) + '\n')
