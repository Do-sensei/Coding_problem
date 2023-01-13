n = int(input())

rev_direction = [[1,3], [2,4], [3,2], [4,1]]

direction = []
h = []
w = []

for _ in range(6):
    d, le = map(int, input().split())
    if d == 1 or d == 2:
        h.append(le)
    else:
        w.append(le)
    direction.append([d, le])
total_area = max(h) * max(w)

for j in range(len(direction)):
    if [direction[j%6][0], direction[(j+1)%6][0]] in rev_direction:
        re_area = direction[j%6][1] * direction[(j+1)%6][1]

print(n*(total_area-re_area))