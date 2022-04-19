N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()
dep_time = -(10**10)
count = 10**10
ret = 0
for t in T:
    if count >= C or dep_time < t:
        count = 1
        dep_time = t + K
        ret += 1
    else:
        count += 1
print(ret)

"""
あり本で見た給油して遠くまで問題に近そう

ソートして貪欲法に見える

逆転するケースはあるだろうか？
密なパターンと疎なパターン


"""
