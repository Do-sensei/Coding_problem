def solution(s):
    s_str_list = s[2:-2].split('},{')
    for k, v in enumerate(s_str_list):
        s_str_list[k] = list(map(int, v.split(',')))
    s_dic = {len(v):v for v in s_str_list}
    sort_s = sorted(s_dic.items(), key=lambda x: x[0], reverse=False)
    result = []
    for i in sort_s:
        for j in i[1]:
            if j not in result:
                result.append(j)
    return result