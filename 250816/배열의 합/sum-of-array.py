arr_2d = [
	list(map(int, input().split()))
	for _ in range(4)
]
	
for i in range(4):
    ans = 0
    for j in range(4):
	    ans += arr_2d[i][j]
    print(ans)
