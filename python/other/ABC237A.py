N = input()
Flag = True
if N[0] == "-":
    l = len(N[1:])
    a = str(1 << 31).zfill(l)
    N.zfill(len(a))
    Flag = a >= N[1:]
else:
    l = len(N)
    a = str(1 << 31).zfill(l)
    N.zfill(len(a))
    Flag = a > N

if Flag:
    print("Yes")
else:
    print("No")
