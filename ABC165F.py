N = int(input())
A = list(map(int, input().split()))

ret = [0] * N

dp = []


"""
何らか再利用ができるイメージ

LISと言えばDPな感じはする
葉が増えたところでdpを伸ばしていくイメージ？
dpをappend/delしつつ、都度結果はストアしていく
再帰のほうが相性よさそう

dp[i][j]=i文字目まで使ってj文字できたときの最小値
再帰で書くとスタック食い切りそう

dfs的にとくとして、
子供から親に戻るときにdpテーブルを復元できるか？
dp[i]で増やすだけだからできそう

逆に保存しようと考えたとき、
N**2ぐらいになるのでは・・・？

dpの設計を変えてみる
dp[i][j]=i文字目まで使って、数字jまで使った時の最大長さ


"""
