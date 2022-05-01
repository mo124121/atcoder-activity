from collections import Counter


N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7
count = Counter(A)

ret = 1
for k, v in count.items():
    if k == 0:
        if v > 1:
            ret = 0
            break
    elif v != 2:
        ret = 0
        break
    else:
        ret = ret * 2 % MOD
print(ret)

"""
なんかグラフっぽい

読み間違えていた
ある人が入れる場所は2個所か1個所(0の場合)
(N-1)//2^2みたいなパターン数になるはず
0を除いて、同じ絶対値に超2人しかいてはいけない


"""
