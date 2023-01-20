def solution(a, b):
    answer = 2
    n, m = a, b
    for i in reversed(range(2, min(a, b)+1)):
        if n % i == 0 and m % i == 0:
            n, m = n//i, m//i
            print(n, m, i)
    if m == 1:
        answer = 1 
    while m != 1:
        if m == 2 or m == 5:
            answer = 1
            break
        elif m % 2 == 0:
            m = m//2
        elif m % 5 == 0:
            m = m//5
        else:
            break
    return answer
