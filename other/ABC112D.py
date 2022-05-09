N, M = map(int, input().split())

for i in range(M // N, 0, -1):
    if M % i == 0:
        print(i)
        exit()

"""
上界 M/N when M%N==0
下界 1

上から貪欲にやってみる？
割り切れたらおしまい、的な

"""
