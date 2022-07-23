m = int(input())

if m < 100:
    print("00")
elif m < 6000:
    print(f"{m//100:02}")
elif m < 35000:
    print(f"{m//1000+50:02}")
elif m <= 70000:
    print(f"{(m//1000-30)//5+80:02}")
else:
    print("89")
