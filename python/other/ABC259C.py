S = input()
T = input()

prev = "Z"
count = 0
S1 = []
for c in S:
    if prev != c and count:
        S1.append((prev, count))
        count = 0
    prev = c
    count += 1
S1.append((prev, count))

prev = "Z"
count = 0
T1 = []
for c in T:
    if prev != c and count:
        T1.append((prev, count))
        count = 0
    prev = c
    count += 1
T1.append((prev, count))


def no():
    print("No")
    exit()


if len(T1) != len(S1):
    no()

for (s, sc), (t, tc) in zip(S1, T1):
    if s != t:
        no()
    if sc != tc:
        if sc == 1 or sc > tc:
            no()

print("Yes")
