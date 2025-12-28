#홀수이면서 3의 배수이거나 짝수이면서 5의수배수

N =int(input())

if (N % 2 == 1 and N % 3 == 0) or (N % 2 == 0 and N % 5 == 0):
    print("true")
else:
    print("false")