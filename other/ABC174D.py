N = int(input())
C = input()

R = []
for i, c in enumerate(C):
    if c == "R":
        R.append(i)
R = set(R)
for r in range(len(R)):
    R.discard(r)

print(len(R))
