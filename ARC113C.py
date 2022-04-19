from collections import defaultdict


S = input()
S = S[::-1]
ret = 0
prev = "0"
prev_c = defaultdict(int)

for i, c in enumerate(S):
    if prev == c:
        ret += i - prev_c[c] - 1
        prev_c.clear()
        prev_c[prev] = i
    else:
        prev_c[prev] += 1
    prev = c


print(ret)

"""
右から見ていって連続したのを見つけたら右からのカウントを足す
"""
