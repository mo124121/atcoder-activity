A = int(input())
B = int(input())
if B % 2 == 0:
    print(int(str(B // 2) + "0" + str(A)))
else:
    print(int(str(B // 2) + "5" + str(A)))
