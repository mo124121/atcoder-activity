N, M = map(int, input().split())
S = input().split()
T = input().split()

kyuukou = {}

for t in T:
    kyuukou[t] = True

for s in S:
    if s in kyuukou:
        print("Yes")
    else:
        print("No")
