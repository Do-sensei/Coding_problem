def solution(lines):
    answer = 0
    arr = []
    for i in lines:
        for j in range(i[0], i[1]):
            arr.append(j)

    set_arr = set(arr)
    for k in set_arr:
        if arr.count(k) > 1:
            answer += 1
    return answer