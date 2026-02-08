A, B = map(int, input().split())

if A>0:
    for _ in range(B):
        print(A, end="")
if A<=0:
    print(0)