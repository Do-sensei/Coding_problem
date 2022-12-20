total_arr = [i+1 for i in range(30)]
for _ in range(28):
    total_arr.remove(int(input()))
    
for j in total_arr:
    print(j)