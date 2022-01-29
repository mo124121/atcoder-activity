S = input()

target = [["i", "I"], ["c", "C"], ["t", "T"]]

i = 0

for c in S:
    if c in target[i]:
        i += 1
    if i == 3:
        print("YES")
        exit()

print("NO")
exit()
