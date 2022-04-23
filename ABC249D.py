from collections import Counter, defaultdict


N = int(input())
A = list(map(int, input().split()))
A.sort()
max_A = max(A)
A_c = Counter(A)


seen = defaultdict(int)
for vj, cj in A_c.items():
    for vk, ck in A_c.items():
        ai = vj * vk
        if ai > max_A:
            break
        seen[ai] += cj * ck

ret = 0
for a in A:
    ret += seen[a]
print(ret)

"""
N<2*10**5
Ai<2*10**5
NlogNとか

Ai/Aj=Ak -> Ai=Aj*Ak (Ai>1なので0は考えない)

因数を考えたくはなる

iを軸に考えるべきか？

ソートした上で、A[i]の因数を構成できるペアを探す
N(i線形)*N(j線形)*1(kの存在有無)
これだとTLE

とりあえずmaxを超える前までのペアを辞書として持っておく
それに該当するの個数が答え

上記操作は調和級数的になるはず
んー間に合わない

"""
