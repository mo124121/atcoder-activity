a, b = map(int, input().split())

if a > 0:
    print("Positive")
elif a <= 0 and b >= 0:
    print("Zero")
else:
    if (b - a) % 2 == 1:
        print("Positive")
    else:
        print("Negative")
