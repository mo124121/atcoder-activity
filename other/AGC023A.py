from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

sum_count = defaultdict(int)
s = 0
sum_count[0] = 1
for a in A:
    s += a
    sum_count[s] += 1

ret = 0
for v in sum_count.values():
    ret += v * (v - 1) // 2

print(ret)

"""
各位置までの和みたいなものが欲しくなる
とりあえず、ひだりから足していった和の出現回数を数える

左から引いて行って、負の和がある出現回数分増やす
ただし負の和を増やすにあたり、カウントを減らしていく

解説後
Si-Sj 

"""
