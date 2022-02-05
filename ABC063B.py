S = input()
seen = {}

for c in S:
    if c in seen:
        print("no")
        exit()
    else:
        seen[c] = 0
print("yes")
