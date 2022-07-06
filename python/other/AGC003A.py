from collections import Counter


S = input()
count = Counter(S)


def no():
    print("No")
    exit()


if "N" in count and "S" not in count:
    no()
if "S" in count and "N" not in count:
    no()
if "W" in count and "E" not in count:
    no()
if "E" in count and "W" not in count:
    no()

print("Yes")
