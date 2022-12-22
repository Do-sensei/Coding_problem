n = int(input())
white = [[0 for _ in range(100)] for _ in range(100)]
cnt = 0

paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

for i in paper:
    for j in range(i[0]-1, i[0]+9):
        for k in range(i[1]-1, i[1]+9):
            white[j][k] = 1

for w in white:
    cnt += w.count(1)

print(cnt)