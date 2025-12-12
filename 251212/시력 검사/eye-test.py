eye_L = float(input())
eye_R = float(input())

if eye_L and eye_R >= 1.0:
    print("High")
elif eye_L and eye_R >= 0.5:
    print("Middle")
else:
    print("Low")