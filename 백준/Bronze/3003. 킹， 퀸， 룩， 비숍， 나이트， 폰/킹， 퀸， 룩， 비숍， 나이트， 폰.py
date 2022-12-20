inp = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
result = []

for i, j in zip(chess, inp):
    a = i - j
    result.append(a)
    # print(a)
    
print(*result)