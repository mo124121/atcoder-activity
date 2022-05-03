from collections import Counter


S = input()
count = Counter(list(S))

if (
    abs(count["a"] - count["b"]) <= 1
    and abs(count["b"] - count["c"]) <= 1
    and abs(count["c"] - count["a"]) <= 1
):
    print("YES")
else:
    print("NO")
