n, m = map(int, input().split())
arr = list(map(int, input().split()))

total_sum = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            card_sum = arr[i] + arr[j] + arr[k]
            if card_sum <= m:
                total_sum.append(card_sum)
                
print(max(total_sum))