import sys
input = sys.stdin.readline

input_str = input().rstrip()
print(1 if input_str == input_str[::-1] else 0)