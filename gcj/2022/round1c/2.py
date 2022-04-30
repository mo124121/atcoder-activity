T = int(input())
ret = []


def calc_sum_sq(A):
    ret = 0
    for a in A:
        ret += a**2
    return ret


for t in range(T):
    N, K = map(int, input().split())
    E = list(map(int, input().split()))
    E_sum = sum(E)
    sq_sum = E_sum**2
    sum_sq = calc_sum_sq(E)

    r = []
    flag = True
    if sq_sum == sum_sq:
        r.append(0)
    elif K == 1:
        if E_sum != 0 and (sum_sq - sq_sum) % (E_sum * 2) == 0:
            e = (sum_sq - sq_sum) // (E_sum * 2)
            r.append(e)
            E.append(e)
            # print("DB:", t, K, sum(E), calc_sum_sq(E))
        else:
            r.append("IMPOSSIBLE")
    else:
        if E_sum == 0:
            r.append(1)
            E.append(1)
        else:
            e = 1 - E_sum
            r.append(e)
            E.append(e)
        E_sum = sum(E)
        sq_sum = E_sum**2
        sum_sq = calc_sum_sq(E)
        if E_sum != 0 and (sum_sq - sq_sum) % (E_sum * 2) == 0:
            e = (sum_sq - sq_sum) // (E_sum * 2)
            r.append(e)
            E.append(e)
            # print("DB:", t, K, sum(E) ** 2, calc_sum_sq(E))
        else:
            r.append("IMPOSSIBLE")

    ret.append(r)


for i, r in enumerate(ret):
    print("Case #{:}:".format(i + 1), *r)


"""
超数学感あるなあ

squaryとはどういうことか？

とりあえず正の数なら
(ΣE)**2>ΣE**2
ただ負の数がある

最大K個追加してなんとかなるのか？

とりあえず1個ならすぐできるしやるか

(x+y)**2-x**2-y**2=2xy

とりあえずtest1は終了
これは今後追加していっても、2の倍数の差じゃないとどうしようもない
2<=Kの時は逆にどうとでも
待て何かおかしい

(a1+a2+a3+x)**2-a1**2-a2**2-a3**2-x**2
=a1*(a2+a3+x)+a2*(a1+a3+x)+a3*(a1+a2+x)+x*(a1+a2+a3)
やっぱりなんかあってそう

とすると1個あればいいわ


"""
