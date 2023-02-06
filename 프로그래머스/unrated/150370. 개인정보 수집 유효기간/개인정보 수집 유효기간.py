def days(ymd):
    one_mon = 28
    new_ymd = ymd.split('.')
    y, m, d = int(new_ymd[0]), int(new_ymd[1]), int(new_ymd[2])
    return y*12*one_mon + m*one_mon + d 

def solution(today, terms, privacies):
    answer = []
    term_dic = {}
    today_days = days(today)
    for i in terms:
        term_dic[i.split()[0]] = i.split()[1]
    for j in range(len(privacies)):
        p_ymd, p_trm = privacies[j].split()
        p_days = days(p_ymd)
        # print(today_days, p_days + int(term_dic[p_trm])*28)
        if p_days -1 + int(term_dic[p_trm])*28 < today_days:
            answer.append(j+1)
    return answer