from itertools import permutations

def solution(babbling):
    answer = 0
    babb_list = ["aya", "ye", "woo", "ma"]
    word_arr = []
    
    for i in range(1, len(babb_list)+1):
        for j in permutations(babb_list, i):
            
            word_arr.append("".join(j))
    
    for k in babbling:
        if k in word_arr:
            answer += 1
            
    return answer