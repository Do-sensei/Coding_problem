import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def divisor(n):
    div = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            div.append(i)
            if i != n//i:
                div.append(n//i)

    div.sort()
    return div

div = divisor(n)
print(div[k-1] if len(div) >= k else 0)