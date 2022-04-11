N = int(input())

st = [[0]]

while len(st):
    s = st.pop()
    if len(s) < N:
        for i in reversed(range(max(s) + 2)):
            st.append(s + [i])
    else:
        print(*list(map(lambda x: chr(x + ord("a")), s)), sep="")
"""
考察
N<10
全パターン 26**10<10**15

広義単調増加的に見える　前の問題にとらわれすぎ

aaa aab aba abb abc

と言いつつ前回同様dequeで解けそう
左側にある文字のmax文字+1まで行ける感じ

文字列なので

"""
