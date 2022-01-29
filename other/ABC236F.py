N = int(input())
c = list(map(int, input().split()))

C = [[c[i], i + 1] for i in range(len(c))]
C.sort()

S = []
ret = 0
cnt = 0
occurence = {}

for i in range(2 ** N):
    if cnt == N:
        break
    if C[i][1] not in occurence:
        new_occurence = {}
        for j in occurence:
            if occurence[j]:
                new_occurence[j ^ C[i][1]] = True
        occurence[C[i][1]] = True
        occurence = {**occurence, **new_occurence}
        ret += C[i][0]
        cnt += 1

print(ret)
