S = input()
count = [0] * 3

for c in S:
    count[ord(c) - ord("a")] += 1

if max(count) - min(count) <= 1:
    print("YES")
else:
    print("NO")


"""
回文判定、難しい

aba x

そもそもすごいせまくない？
aa x

abcabc...
が続けられるかどうか
各文字カウント->max-min<=1

"""
