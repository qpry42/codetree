# 변수 선언, 입력
a_math, a_eng = map(int, input().split())
b_math, b_eng = map(int, input().split())

# 출력
if a_math > b_math and a_eng > b_eng:
	print(1)
else:
	print(0)
