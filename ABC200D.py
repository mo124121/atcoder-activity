N = int(input())
A = list(map(int, input().split()))

seen = {0: []}
tmp = {}
for i, a in enumerate(A):
    tmp.clear()
    for k, v in seen.items():
        kn = (k + a) % 200
        tmp[kn] = seen[k] + [i + 1]
        if kn in seen:
            tmp[kn] = seen[k] + [i + 1]
            if len(tmp[kn]) == N:
                print("No")
            else:
                if len(seen[kn]) == 0:
                    for j in range(1, N + 1):
                        if j not in tmp[kn]:
                            seen[kn].append(j)
                            tmp[kn].append(j)
                            break
                print("Yes")
                print(len(seen[kn]), *sorted(seen[kn]))
                print(len(tmp[kn]), *sorted(tmp[kn]))
                exit()

    for k, v in tmp.items():
        if k not in seen:
            seen[k] = tmp[k]
print("No")


"""
回答空間が広そうな問題
modの空間で0が作れるものが存在すればOK
"""
