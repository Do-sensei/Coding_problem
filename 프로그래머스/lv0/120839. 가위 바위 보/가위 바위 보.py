def solution(rsp):
    vic_rsp = {'2':'0', '0':'5', '5':'2'}
    
    answer = ''
    for i in rsp:
        answer += vic_rsp[i]
    return answer