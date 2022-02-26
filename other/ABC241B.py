from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

l_count = defaultdict(int)
for a in A:
    l_count[a] += 1

ret = "Yes"
for b in B:
    if l_count[b] == 0:
        ret = "No"
        break
    else:
        l_count[b] -= 1

print(ret)
