N, K, X = map(int, input().split())
A = list(map(int, input().split()))

ret = 0
B = []
for a in A:
    max_k = a // X
    max_k = min(K, max_k)
    K -= max_k
    b = a - max_k * X
    ret += b
    B.append(b)
B.sort(reverse=True)
for b in B:
    if K > 0:
        ret -= b
        K -= 1
    else:
        break

print(ret)
