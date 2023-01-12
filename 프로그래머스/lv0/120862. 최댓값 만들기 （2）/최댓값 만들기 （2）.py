def solution(numbers):
    answer = -100000000000
    for a, i in enumerate(numbers):
        for b, j in enumerate(numbers):
            if a == b:
                continue
            if i * j >= answer:
                answer = i * j
    return answer