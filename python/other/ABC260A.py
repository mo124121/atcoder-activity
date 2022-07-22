from collections import Counter


S = input()
count = Counter(S)
for k, v in count.items():
    if v == 1:
        print(k)
        exit()
print(-1)
