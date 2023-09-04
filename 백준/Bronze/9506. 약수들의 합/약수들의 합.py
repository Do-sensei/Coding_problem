import sys
input = sys.stdin.readline

def divisor(n):
    div = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            div.append(i)
            if i != n//i:
                div.append(n//i)

    div.sort()
    return div

while True:
    n = int(input())
    if n == -1:
        break
    div = divisor(n)
    div.pop()
    if sum(div) == n:
        print(f"{n} = {' + '.join(map(str, div))}")
    else:
        print(f"{n} is NOT perfect.")