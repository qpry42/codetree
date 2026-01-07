A_age, A_sex = input().split()
B_age, B_sex = input().split()

A_age = int(A_age)
B_age = int(B_age)
A_sex = str(A_sex)
B_sex = str(B_sex)

if A_age >= 19 or B_age >= 19:
    if A_sex == "M" or B_sex == "M":
        print(1)
    
    elif A_sex =="W" or B_sex == "W":
        print(0) 
else:
    print(0)

        