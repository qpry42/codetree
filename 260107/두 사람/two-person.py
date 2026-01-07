A_age, A_sex = input().split()
B_age, B_sex = input().split()

A_age = int(A_age)
B_age = int(B_age)
A_sex = str(A_sex)
B_sex = str(B_sex)

if A_age >= 19 and A_sex == "M" or B_age >= 19 and B_sex == "M":
    print(1)
else:
    print(0)

#list를 쓰면 위보다 간략하게 쓸 수 있다.
'''a=list(input().split())
b=list(input().split())
if int(a[0])>=19 and a[1]=="M" or int(b[0])>=19 and b[1]=="M":
    print(1)
else:
    print(0)'''


'''두사람의 나이와 성별
1. 둘 중 하나라도 19세 이상
1-1. 남자면 1
1-2 둘다 여자면 0 
2. 둘 다 19세 미만이라면 0
'''
