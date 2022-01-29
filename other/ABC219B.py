s=[""]*3
s[0]=input()
s[1]=input()
s[2]=input()
T=input()

for t in T:
    print(s[int(t)-1],end="")
print("")