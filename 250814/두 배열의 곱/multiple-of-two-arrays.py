arr_1 = [
	list(map(int, input().split()))
	for _ in range(3)
]

input()

arr_2 = [
	list(map(int, input().split()))
	for _ in range(3)
]

arr_3 = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3):
	for j in range(3):
		arr_3[i][j] = arr_1[i][j] * arr_2[i][j]
	
for i in range(3):        
    for j in range(3):    
        print(arr_3[i][j], end=" ")
    print()
