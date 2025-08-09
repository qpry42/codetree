n = int(input())

for i in range(n):
	inp = input()
	arr = inp.split()
	a, b = int(arr[0]), int(arr[1])

	ans = 0
	
	for j in range(a, b + 1):
		if j % 2 == 0:
			ans += j
	
	print(ans)
