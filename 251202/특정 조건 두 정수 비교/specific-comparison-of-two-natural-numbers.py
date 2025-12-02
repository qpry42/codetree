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

''' 변수 선언, 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

# 출력
if a < b:
	print("1", end=" ")
else:
	print("0", end=" ")
if a == b:
	print("1")
else:
	print("0")

✨ end=" "의 역할

print("1", end=" ")는
출력 결과를 1 뒤에 공백을 붙이고 줄바꿈을 하지 않는다는 뜻이야.'''