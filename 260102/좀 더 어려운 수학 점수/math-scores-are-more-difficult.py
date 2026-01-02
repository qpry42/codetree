A_Math, A_Eng = map(int, input().split())
B_Math, B_Eng = map(int, input().split())

if A_Math > B_Math:
    print("A")
elif A_Math < B_Math:
    print("B")

if A_Math == B_Math and A_Eng > B_Eng:
    print("A")
elif A_Math == B_Math and A_Eng < B_Eng:
    print("B")