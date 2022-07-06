s = input()
s = s.replace("BC", "D")
N = len(s)
a_count = 0
ret = 0
prev = "A"
for i in range(N):
    c = s[i]
    if prev == "A" and c == "D":
        ret += a_count
        prev = "A"
        continue

    if c == "A":
        a_count += 1
    else:
        a_count = 0
    prev = c

print(ret)


"""
尺取り法っぽい
左から走査していって、bcを見つけたら左に続くaの数分動かせる
逆にa,bc以外のものを見つけたらAの数をリセットする

解説後
bcはセットなので、別の文字(d)に置き換えてよい
"""
