A, B, C = map(int, input().split())

if A <= B:
    if B <= C:
        print(B)
    elif A <= C:
        print(C)
    else:
        print(A)
else:
    if A <= C:
        print(A)
    elif B <= C:
        print(C)
    else:
        print(B)          
