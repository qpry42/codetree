#10개를 저장할 수 있는 배열을 만들고 10개의 문자를 입력 받고 
#입력받은 문자들을 입력받은 순서의역순으로 출력하는 프로그램


arr = list(input().split())

for i in range(9, -1, -1):
    print(arr[i], end="")
