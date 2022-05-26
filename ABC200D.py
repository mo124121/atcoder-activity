from itertools import product


N = int(input())
A = list(map(int, input().split()))

seen = {}

l = min(8, len(A))
for pat in product((True, False), repeat=l):
    b = [i + 1 for i in range(l) if pat[i]]
    if not b:
        continue
    x = sum([A[i] for i in range(l) if pat[i]]) % 200
    if x in seen:
        print("Yes")
        print(len(seen[x]), *seen[x])
        print(len(b), *b)
        exit()
    else:
        seen[x] = b

print("No")


"""
回答空間が広そうな問題
modの空間で0が作れるものが存在すればOK

解説が賢すぎる

"""
