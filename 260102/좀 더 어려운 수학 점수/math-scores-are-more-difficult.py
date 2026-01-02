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


"""A_math, A_eng = map(int, input().split())
B_math, B_eng = map(int, input().split())

if A_math > B_math :
    print("A")
elif B_math > A_math :
    print("B")
else :
    if A_eng > B_eng :
        print("A")
    else :
        print("B")"""
