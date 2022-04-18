b, c = map(int, input().split())

l = b - c // 2
r = b
if c >= 2:
    r = b + (c - 2) // 2

b = -b
c -= 1
p = b - c // 2
q = b + c // 2

ans = r - l + 1 + q - p + 1

u = max(l, p)
v = min(r, q)
if u <= v:
    ans -= v - u + 1

print(ans)


"""
DPで…と思ったけどNがでかい

ただまあ場合分けな気はする
絶対値として移動するには2円払うしかない


abs(B)>C//2


絶対めんどくさいと思って解法読んでしまった

反転側・反転しない側でとる範囲を計算して、重複する部分を削除する感じ

"""
