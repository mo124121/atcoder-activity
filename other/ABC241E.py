from collections import defaultdict


N, K = map(int, input().split())
A = list(map(int, input().split()))

count = defaultdict()
num = 0
count[num] = 0
one_way = [(num, num)]
loop = []
for i in range(K):
    num += A[num % N]
    one_way.append((num % N, num))
    if num % N in count:
        num_n = num + A[num % N]
        loop = one_way[count[num % N] + 1 :]
        one_way = one_way[: count[num % N] + 1]
        break
    count[num % N] = i + 1

ret = one_way[-1][1]
if K + 1 == len(one_way):
    print(ret)
    exit()

loop_sum = loop[-1][1] - ret

ret += loop_sum * ((K - len(one_way)) // len(loop))

ret += loop[(K - len(one_way)) % len(loop)][1] - one_way[-1][1]

print(ret)
