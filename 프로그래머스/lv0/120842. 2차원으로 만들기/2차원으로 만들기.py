def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        ans = []
        for j in range(i, i+n):
            ans.append(num_list[j])
        answer.append(ans)
    return answer