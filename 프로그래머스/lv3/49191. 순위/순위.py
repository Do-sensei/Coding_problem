def solution(n, results):
    answer = 0
    wins = {i: set() for i in range(1, n+1)}
    loses = {i: set() for i in range(1, n+1)}

    for winner, loser in results:
        wins[winner].add(loser)
        loses[loser].add(winner)

    for i in range(1, n+1):
        for winner in loses[i]:
            wins[winner].update(wins[i])
        for loser in wins[i]:
            loses[loser].update(loses[i])

    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n-1:
            answer += 1

    return answer