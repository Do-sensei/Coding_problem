def solution(board):
    safe_area = [[1 if 0<i<len(board)+1 else 0 for i in range(len(board)+2)] 
                 if 0<j<len(board)+1 else [0 for i in range(len(board)+2)] 
                 for j in range(len(board)+2)]
    
    answer = 0
    for i, n in enumerate(board):
        for j, m in enumerate(n):
            if m == 1:
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        safe_area[k][l] = 0

    for i in safe_area:
        answer += sum(i)
    return answer