def solution(a, b):
    answer = 0
    n = abs(a-b)+1
    answer = n*(a+b)//2
    return answer