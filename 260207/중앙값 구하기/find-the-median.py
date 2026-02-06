A, B, C = map(int,input().split())

#A가 중앙값일 때,
#A는 B보다 크고 C보다 작거나. C보다 크고 B보다 작거나

if A >= B and A <= C or A <= B and A >= C:
    print(A)
elif B >=A and B <= C or B <= A and B >= C:
    print(B)
else:
    print(C)
