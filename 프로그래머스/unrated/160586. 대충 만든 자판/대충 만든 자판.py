def solution(keymap, targets):
    answer = []
    key_dic = {}
    for i in keymap:
        for j in i:
            if j not in key_dic.keys():
                key_dic[j] = i.index(j)
            elif j in key_dic.keys():
                if key_dic[j] > i.index(j):
                    key_dic[j] = i.index(j) 
            
    for k in targets:
        cnt = 0
        for l in k:
            if l in key_dic.keys():
                cnt += key_dic[l] +1
            elif l not in key_dic.keys():
                cnt = -1
                break
            
        answer.append(cnt)
    return answer
