A, B = map(int, input().split())

if B >= A:
    for i in range(B, A-1, -1):
        print(i, end=" ")
elif A >= B:
    for i in range(A, B-1, -1):
        print(i, end=" ")

'''inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
map 대신에 이 거 써도 됨'''