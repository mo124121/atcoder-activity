from collections import Counter


N = int(input())

myoji = Counter()
namae = Counter()

ST = [input().split() for _ in range(N)]

for s, t in ST:
    myoji[s] += 1
    namae[t] += 1

for s, t in ST:
    if s == t:
        if myoji[s] == 1 and namae[s] == 1:
            continue
    else:
        if myoji[s] == 1 and namae[s] == 0:
            continue
        if myoji[t] == 0 and namae[t] == 1:
            continue
    print("No")
    exit()

print("Yes")
