def solution(n):
    n_lst = list(int(i) for i in str(n))
    n_lst.sort(reverse=True)
    answer = int(''.join(str(i) for i in n_lst))
    return answer