import sys
import math
n, m = map(int,input().split(" "))

l = [True for i in range(m + 1)] 

for i in range(2, int(math.sqrt(m)) + 1):
    if l[i] == True:
        j = 2 
        while i * j <= m:
            l[i * j] = False
            j += 1

for i in range(n, m + 1):
    if l[i]:
        if i != 1:
            print(i)