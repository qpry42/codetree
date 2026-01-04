# 변수 선언, 입력
y = int(input())

# 출력
if y % 4 == 0:
	if y % 100 == 0:
		if y % 400 == 0:
			print("true")  #4, 100, 400 나머지가 0일 때 윤년
		else:
			print("false") #400은 안될 때 평년
	else:
		print("true") #4로만 나뉠 때 윤년
else:
	print("false") #4도 안될때




