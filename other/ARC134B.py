from collections import Counter


N = int(input())
S = list(input())

count = Counter(S)

j = N - 1
for i in range(N):
    count[S[i]] -= 1
    target_char = S[i]
    for k in count.keys():
        if count[k] > 0 and target_char > k:
            target_char = k
    if target_char == S[i]:
        continue

    j2 = j
    count2 = Counter()
    while i < j2 and S[j2] != target_char:
        count2[S[j2]] += 1
        j2 -= 1
    if S[j2] == target_char:
        count2[S[j2]] += 1
        S[i], S[j2] = S[j2], S[i]

        for k, v in count2.items():
            count[k] -= v
        j = j2 - 1

print(*S, sep="")
