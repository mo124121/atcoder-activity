from functools import lru_cache


@lru_cache(maxsize=None)
def fib(x):
    if x <= 2:
        return x
    else:
        return fib(x - 1) + fib(x - 2)


K = int(input())
A = fib(K + 1)
B = fib(K)
print(A, B)


"""
逆構成の問題か
素数を追加してったら行けそう1

フィボナッチ数列っぽい
AC

解説後
KがMAXのときの出力範囲が正しいかは見ておくべき

"""
