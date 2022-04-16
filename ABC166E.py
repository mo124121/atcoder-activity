from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

B = defaultdict(int)
C = defaultdict(int)

for i in range(N):
    B[-A[i] - i - 1] += 1
    C[A[i] - i - 1] += 1

ret = 0
for k, v in B.items():
    ret += v * C[k]

print(ret)

"""
考察
N<2*10**5
NlogNあたりまで

二つのキーがあって一致するのを探すイメージ
差の絶対値がN**2パターンある、こっちの探索はできない
和もN**2あるくない？

Aをソートして2分探索するとか？なんか違う気がする

グラフ的に考えてみる・・・
条件を満たすときにつながるイメージ

abs(i-j)=A[i]+A[j]
if i>j:
    A[i]-i=-A[j]-j
else:
    A[i]+i=-A[j]+j

abs(i-j)-A[j]=A[i]


辞書的なものを使いたい　差がXの辞書と和がAの辞書　結局登録に時間がかかる

いっそB[i]=A[i]-iとかしたら？

"""
