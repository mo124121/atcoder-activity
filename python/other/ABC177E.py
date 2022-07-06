from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
MAX_A = 10**6
is_prime = [True] * (MAX_A + 1)
is_prime[0] = is_prime[1] = False
factor = defaultdict(set)
i = 2
while i <= MAX_A:
    if is_prime[i]:
        j = i * 2
        while j <= MAX_A:
            is_prime[j] = False
            factor[j].add(i)
            j += i
    i += 1


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


coprime = A[0]
seen = set()
seen.add(1)
flag = True
for a in A:
    coprime = gcd(coprime, a)
    if is_prime[a]:
        if a in seen:
            flag = False
            break
        seen.add(a)
    else:
        for b in factor[a]:
            if b in seen:
                flag = False
                break
            seen.add(b)
if flag:
    print("pairwise coprime")
elif coprime == 1:
    print("setwise coprime")
else:
    print("not coprime")

"""
pairwise coprime:全組み合わせが互いに素
setwise coprime:どこかに最大公約数が1の組み合わせがある

N<10**6
Ai<10**6

Aiが微妙に小さくて素数的な計算をせよとのメッセージ
pairwiseのためには素因数が他で出てきてはいけない->辞書で管理する感じ

setwiseはそれぞれ出てきた素因数について、
その素因数を持たない数がどこかにある感じ

ふるいを使うときに、同時にどんな約数が混じるか確認できる？
サイズ的に間に合うか？まあ何とかなるんじゃね


"""
