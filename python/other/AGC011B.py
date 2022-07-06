N = int(input())
A = list(map(int, input().split()))
A.sort()
ret = 0
prev = 0
for a in A:
    if prev * 2 < a:
        ret = 0
    ret += 1
    prev += a
print(ret)
"""
小さい方から足していくイメージ
足していって、2倍以上差があった時には色はリセット

"""
