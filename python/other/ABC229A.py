S1 = input()
S2 = input()


def no():
    print("No")


if S1 == "#." and S2 == ".#":
    no()
elif S2 == "#." and S1 == ".#":
    no()
else:
    print("Yes")
