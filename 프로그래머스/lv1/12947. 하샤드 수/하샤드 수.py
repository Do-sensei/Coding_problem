def solution(x):
    answer = True
    str_lst_x = list(int(i) for i in str(x))
    sum_x = sum(str_lst_x)
    if x % sum_x != 0:
        answer = False
    return answer