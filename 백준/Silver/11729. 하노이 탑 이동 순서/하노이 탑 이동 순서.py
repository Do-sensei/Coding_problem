def hanoi_top(n, a, b):
    if n == 1:
        print(a, b)
        return
    
    hanoi_top(n-1, a, 6-a-b)
    print(a, b)
    hanoi_top(n-1, 6-a-b, b)
    
n = int(input())
print(2**n-1)
hanoi_top(n, 1, 3)