S = input()

while True:
    if S[-5:]=="dream":
        S = S[:-5]
    elif S[-7:]=="dreamer":
        S = S[:-7]
    elif S[-5:]=="erase":
        S = S[:-5]
    elif S[-6:]=="eraser":
        S = S[:-6]
    else:
        break

if len(S)==0:
    print("YES")
else:
    print("NO")