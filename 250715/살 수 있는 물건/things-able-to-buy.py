mulgun = ["book", "mask"]
#price = [3000, 1000]

N = int(input())

if N >= 3000:
    print(mulgun[0])
elif 1000 <= N < 3000:
    print(mulgun[1])
else:
    print("no")