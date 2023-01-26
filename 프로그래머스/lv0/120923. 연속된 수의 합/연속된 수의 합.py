def solution(num, total):
    answer = []
    n = total // num
    length = num // 2
    if num % 2 == 0:
        for i in range(n-length+1, n+length+1):
            answer.append(i)
    else:
        for i in range(n-length, n+length+1):
            answer.append(i)
    return answer