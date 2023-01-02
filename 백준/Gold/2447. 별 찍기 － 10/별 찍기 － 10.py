def star(x):
    if x == 1:
        return ['*']
    
    stars = star(x//3)
    arr = []

    for i in stars:
        arr.append(i*3)

    for j in stars:
        arr.append(j+' '*(x//3)+j)
    
    for k in stars:
        arr.append(k*3)

    return arr

n = int(input())
print('\n'.join(star(n)))