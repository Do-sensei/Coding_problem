def solution(n):
    not_prime = []
    answer = 0
    for i in range(2, n+1):
        for j in range(1, i+1):
            if i % j == 0:
                not_prime.append(i)
        if not_prime.count(i) >= 3:
            answer += 1
    return answer