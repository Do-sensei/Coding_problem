def solution(N, stages):
    len_stage = len(stages)
    result_dic = {}
    for i in range(1, N+1):
        if len_stage != 0:
            cnt = stages.count(i)
            result_dic[i] = cnt / len_stage
            len_stage -= cnt
        else:
            result_dic[i] = 0
    answer = sorted(result_dic, key=lambda x : result_dic[x], reverse=True)
    return answer