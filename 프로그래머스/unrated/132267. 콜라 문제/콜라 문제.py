def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += divmod(n,a)[0]* b
        n = divmod(n,a)[0]* b + divmod(n,a)[1]
    return answer