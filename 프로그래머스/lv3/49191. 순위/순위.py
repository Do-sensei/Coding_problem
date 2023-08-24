# def solution(n, results):
#     answer = 0
#     wins = {i: set() for i in range(1, n+1)}
#     loses = {i: set() for i in range(1, n+1)}

#     for winner, loser in results:
#         wins[winner].add(loser)
#         loses[loser].add(winner)

#     for i in range(1, n+1):
#         for winner in loses[i]:
#             wins[winner].update(wins[i])
#         for loser in wins[i]:
#             loses[loser].update(loses[i])

#     for i in range(1, n+1):
#         if len(wins[i]) + len(loses[i]) == n-1:
#             answer += 1

#     return answer

def solution(n, results):
    # 승패 행렬 초기화
    INF = float('inf')
    matrix = [[INF] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 0

    # 승패 관계 설정
    for win, lose in results:
        matrix[win-1][lose-1] = 1
        matrix[lose-1][win-1] = -1

    # 플로이드-워셜 알고리즘
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] == 1 and matrix[k][j] == 1:
                    matrix[i][j] = 1
                elif matrix[i][k] == -1 and matrix[k][j] == -1:
                    matrix[i][j] = -1

    # 순위를 확정할 수 있는 선수의 수 계산
    count = 0
    for i in range(n):
        if matrix[i].count(1) + matrix[i].count(-1) == n - 1:
            count += 1

    return count
