from collections import Counter


S = input()
occur = Counter(S)
odd_alph = 0
even_count = 0

for k, v in occur.items():
    if v % 2 == 1:
        odd_alph += 1
    even_count += v // 2

if odd_alph == 0:
    print(even_count * 2)
else:
    print(1 + even_count // odd_alph * 2)

"""
len(S)<10**5

回文の条件って右から読んでも左から読んでも１つ
文字が2の倍数（＋奇数長の場合はどれかが奇数)

奇数個分の分割が必要になる


"""
