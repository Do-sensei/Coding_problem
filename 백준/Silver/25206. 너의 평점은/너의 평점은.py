score_dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

total = 0
cnt = 0
while True:
    try:
        line = input().strip()
        if not line:
            break
        _, b, c = line.split()
        b = float(b)
        if c == 'P':
            continue
        c = score_dic.get(c, None)
        if c is None:
            continue
        cnt += b
        total += b * c
    except EOFError:
        break

if cnt == 0:
    print("0.00")
else:
    print('%.6f' % (total / cnt))
