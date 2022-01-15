A, B = map(int, input().split())

ret = False

if A % 3 == 0:
    ret = True
elif B % 3 == 0:
    ret = True
elif (A + B) % 3 == 0:
    ret = True

if ret:
    print("Possible")
else:
    print("Impossible")
