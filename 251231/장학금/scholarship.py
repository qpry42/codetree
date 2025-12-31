M, F = map(int,input().split())

if M >= 90 and F >= 95:
    print(100000)
elif M >= 90 and F >= 90:
    print(50000)
else:
    print(0)