import sys
input = sys.stdin.readline

n = int(input())

company = set()

for _ in range(n):
    n, s = input().split()
    if s == 'enter':
        company.add(n)
    else:
        company.remove(n)

company = sorted(company, reverse=True)
for c in company:
    print(c)