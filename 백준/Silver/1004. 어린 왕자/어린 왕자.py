n = int(input())

def dist(x1, x2, y1, y2):
    return (((x1 - x2)**2 + (y1 - y2)**2)**0.5)

for _ in range(n):
    s_x, s_y, e_x, e_y = map(int, input().split())
    s_cnt = 0
    e_cnt = 0
    s_e_cnt = 0
    m = int(input())
    for _ in range(m):
        x, y, r = map(int, input().split())
        
        if dist(s_x, x, s_y, y) < r and dist(e_x, x, e_y, y) < r:
            s_cnt += 1
            e_cnt += 1
            s_e_cnt += 2
        elif dist(s_x, x, s_y, y) < r:
            s_cnt +=1

        elif dist(e_x, x, e_y, y) < r:
            e_cnt += 1

    print(s_cnt + e_cnt - s_e_cnt)