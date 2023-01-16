def solution(spell, dic):
    answer = 2
    
    for i in dic:
        a = 0
        for j in spell:
            if j in i:
                a += 1
        if a == len(spell):
            answer = 1
            break
    
    return answer