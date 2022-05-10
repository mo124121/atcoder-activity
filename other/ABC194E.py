from collections import Counter, deque


N, M = map(int, input().split())
A = list(map(int, input().split()))

q = deque(A[:M])
count = Counter(A[:M])

for i in range(N + 1):
    if i not in count:
        ret = i
        break

for a in A:
    count[a] += 1
    q.append(a)

    b = q.popleft()
    count[b] -= 1
    if count[b] == 0:
        ret = min(ret, b)


print(ret)

"""
zobrist has使いたくなる問題

orderset使う問題に見える
いや違うな…


数列の中で歯抜けを探すイメージ
重複のある数列

1.5**10**6

これ自体はメモリに乗る

何かいいかえはできないか？

ある数字がi番目に現れたら、i+M番目までは有効になる
出現indexと、存在可能な数字の有無をそれぞれheapで管理してみる？
消失indexのほうが正しいこれはdeque
加えて出現数カウントもしておく？

5WA/26
コーナケースっぽいなあ
AC

解説
もっとシンプルっぽい

"""
