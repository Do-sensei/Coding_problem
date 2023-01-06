def solution(my_string):
    answer = 0
    for i in my_string:
        if str.isdigit(i):
            answer += int(i)
    return answer