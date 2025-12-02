a, b = map(int, input().split())

if a < b :
    N = 1
else:
    N = 0

if a == b:
    S = 1
else:
    S = 0

print(N, S)