R, C, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]

ret = 0
for r in range(R):
    for c in range(C):
        d = r + c
        if d <= D and (D - d) % 2 == 0:
            ret = max(ret, A[r][c])
print(ret)
"""
チェック柄の位置にだけたどりつける

..#..
.#.#.
#.S.#
.#.#.
..#..
偶奇で反転はする
全探索で距離の偶奇とD以内であることをチェックすればいい

"""
