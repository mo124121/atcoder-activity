S = input()
K = int(input())
ret = []
a_ord = ord("a")
for c in S:
    cost = a_ord - ord(c) + 26
    if c != "a" and cost <= K:
        c = "a"
        K -= cost
    ret.append(c)

last = (ord(ret[-1]) - ord("a") + K) % 26

ret[-1] = chr(ord("a") + last)
print("".join(ret))

"""
こーなケースがややこしそう

上位文字からaにできるか試していく
あまりそうなら最後の文字で使う
めっちゃ余るケースがあるやん…

"""
