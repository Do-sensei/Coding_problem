def solution(my_string):
    arr = "aeiou"
    answer = my_string
    for i in arr:
        answer = answer.replace(i, '')
    
    return answer