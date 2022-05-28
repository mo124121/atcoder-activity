from numpy import append


N = int(input())
A = list(map(int, input().split()))

ret = []
gold = True
prev = 0
for i in range(N - 1):
    if A[i] == A[i + 1]:
        ret.append(0)
        continue
    else:
        prev = A[i]

    if gold:
        if prev <= a:
            ret.append(0)
        else:
            ret.append(1)
            gold = False
    else:
        if prev >= a:
            ret.append(0)
        else:
            ret.append(1)
            gold = True
    prev = a
if not gold:
    ret.append(1)
else:
    ret.append(0)
print(*ret)


"""
株の売買問題

上げる時、下げるときをトリガに換金する
問題は最後

同じ時どうする？
経路圧縮しとくのが楽？

"""
