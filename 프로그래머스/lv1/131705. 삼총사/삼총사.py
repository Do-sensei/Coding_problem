from itertools import combinations

def solution(number):
    answer = 0
    comb_arr = combinations(number, 3)
    
    for i in comb_arr:
        if sum(i) == 0:
            answer += 1
    return answer