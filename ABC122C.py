N, Q = map(int, input().split())
S = input()
WORD = "AC"
counter = [0] * (N)
for i in range(N - 1):
    if S[i : i + 2] == WORD:
        counter[i + 1] = 1
    counter[i + 1] += counter[i]

ret = []
for i in range(Q):
    l, r = map(int, input().split())
    re = counter[r - 1] - counter[l - 1]
    ret.append(re)

print(*ret, sep="\n")


"""
超fenwickっぽいけど
まあ事前にカウントしておいたらよさそう
2文字というのが厄介ではある
とりあえず全部探すか
"""
