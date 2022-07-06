s = int(input().replace(" ", ""))

flag = False
for i in range(1000):
    if i**2 == s:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")
