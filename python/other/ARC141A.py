def solve(N):

    r = int((len(N) - 1) * "9")
    for i in range(1, len(N) // 2 + 1):
        if len(N) % i == 0:
            init_ = int(N[:i])
            v = init_
            for j in range(1, len(N) // i):
                v = v * 10**i + init_
            if v <= int(N):
                r = max(r, v)
            elif len(str(init_ - 1)) == len(str(init_)):
                r = max(r, int(str(init_ - 1) * (len(N) // i)))
    return r


def main():
    T = int(input())
    ret = []
    for i in range(T):
        N = input()
        r = solve(N)
        ret.append(r)
    print(*ret, sep="\n")


main()


def naive(N):
    N = int(N)
    ret = 0
    for i in range(11, N + 1):
        l = len(str(i))
        for j in range(1, l // 2 + 1):
            if l % j == 0:
                if int(str(i)[:j] * (l // j)) == i:
                    ret = i
                    break
    return ret


for i in range(11, 5000):
    N = str(i)
    nai = naive(N)
    sol = solve(N)
    if nai != sol:
        print(N, nai, sol)

"""
T<10**4

事前計算できるパターンっぽい

2個以上連結

長さ

"""
