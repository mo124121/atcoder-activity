from itertools import product


N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

flag = False

for cs in product(range(K), repeat=N):
    tmp = T[0][cs[0]]
    for i in range(1, N):
        tmp ^= T[i][cs[i]]
    if tmp == 0:
        flag = True

if flag:
    print("Found")
else:
    print("Nothing")
