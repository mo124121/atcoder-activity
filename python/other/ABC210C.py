from collections import Counter


N, K = map(int, input().split())
C = list(map(int, input().split()))

count = Counter(C[:K])
ret = len(count)

for i in range(K, N):
    count[C[i]] += 1
    count[C[i - K]] -= 1
    if count[C[i - K]] == 0:
        del count[C[i - K]]
    ret = max(len(count), ret)
print(ret)
