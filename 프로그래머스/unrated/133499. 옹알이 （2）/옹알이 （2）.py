def solution(babbling):
    answer = 0
    babb_dict = {"aya":1, "ye":2, "woo":3, "ma":4}
    word_arr = []
    sub_cnt = 0
    for i in babbling:
        a = i
        for j in babb_dict.items():
            a = a.replace(j[0], str(j[1]))
        if a.isdecimal():
            word_arr.append(a)
    for i in word_arr:
        for j in range(len(i)-1):
            if i[j] == i[j+1]:
                sub_cnt += 1
                break
    
    answer = len(word_arr) - sub_cnt
    
    return answer