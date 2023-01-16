import re
def solution(my_string):
    new_string = re.sub("[A-Za-z]", " ", my_string)
    answer =  sum(list(map(int, new_string.split())))

    return answer