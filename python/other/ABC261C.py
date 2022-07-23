from collections import Counter


N = int(input())
count = Counter()

for i in range(N):
    S = input()
    if count[S] == 0:
        print(S)
    else:
        print(f"{S}({count[S]})")
    count[S] += 1
