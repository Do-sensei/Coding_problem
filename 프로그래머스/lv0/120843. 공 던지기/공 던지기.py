def solution(numbers, k):
    answer = 0
    numbers = numbers * 2
    a = (2*(k-1)) % len(numbers) 
    answer = numbers[a]
    return answer