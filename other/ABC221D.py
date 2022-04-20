N = int(input())
in_out = []
for i in range(N):
    a, b = map(int, input().split())
    in_out.append((a, 1))
    in_out.append((a + b, -1))
in_out.sort()
ret = [0] * (N + 1)
day_prev = 0
count = 0
for day, op in in_out:
    ret[count] += day - day_prev
    count += op
    day_prev = day

print(*ret[1:])


"""
bit->いやメモリに乗らない

座標圧縮っぽくはある
いもすっぽくもある

Aを+1
A+Bを-1
としてソート、k人の区間をカウント
"""
