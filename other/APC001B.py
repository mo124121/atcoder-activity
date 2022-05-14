from collections import deque


def yes():
    print("Yes")
    exit()


def no():
    print("No")
    exit()


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = [B[i] - A[i] for i in range(N)]

q = deque(sorted(C, reverse=True))

l = q.popleft()
if len(q) == 0:
    if l >= 0:
        yes()
    else:
        no()
r = q.pop()

while len(q):
    ops = l // 2
    if ops + r > 0:
        l += r * 2
        r = q.pop()

    else:
        l = q.popleft()
        r += ops

if l // 2 + r >= 0:
    yes()
else:
    no()


"""
結局小さいほうから当てはめていくほかない
逆転しているやつがあったらng
誤読乙

発想は貪欲的になるはず
逆転してしまっているbに追加していくイメージ
まず、両方ソートして差を0につぶしていく形
差が正に大きい分を、負に小さい分でつぶしてく
負が消えれば勝ち、でなければダメ
"""
