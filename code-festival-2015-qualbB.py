from typing import Counter


N, M = map(int, input().split())
A = list(map(int, input().split()))

count = Counter(A)

for k, v in count.items():
    if v > N // 2:
        print(k)
        exit()
print("?")
