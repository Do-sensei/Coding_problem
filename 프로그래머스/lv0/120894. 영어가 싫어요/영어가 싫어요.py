def solution(numbers):
    alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, j in enumerate(alpha):
        numbers = numbers.replace(j, str(i))
    
    answer = int(numbers)
    return answer