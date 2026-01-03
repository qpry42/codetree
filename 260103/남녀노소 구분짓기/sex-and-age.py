A_sex = int(input())
A_age = int(input())

if A_sex == 0:
    if A_age >= 19:
        print("MAN")
    else:
        print("BOY")

if A_sex == 1:
    if A_age >= 19:
        print("WOMAN")
    else:
        print("GIRL")