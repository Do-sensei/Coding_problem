from string import ascii_lowercase
def solution(s, skip, index):
    answer = ''
    alp_lst = list(ascii_lowercase)
    for i in skip:
        alp_lst.remove(i)
    for j in s:
        answer += alp_lst[(alp_lst.index(j)+index)%len(alp_lst)]    
    return answer