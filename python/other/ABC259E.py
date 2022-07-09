def solve(N, MPE):
    count = {}
    for i in range(N):
        for p, e in MPE[i]:
            if p not in count:
                count[p] = (0, False)
            if count[p][0] < e:
                count[p] = (e, True)
            elif count[p][0] == e:
                count[p] = (e, False)

    ret = 0
    no_dec = False
    for i in range(N):
        flag = False
        for p, e in MPE[i]:
            if count[p][0] == e and count[p][1]:
                flag = True
                break
        if flag:
            ret += 1
        else:
            no_dec = True
    if no_dec:
        ret += 1

    return ret


def main():
    N = int(input())

    MPE = []

    for i in range(N):
        m = int(input())
        tmp = []
        for j in range(m):
            p, e = map(int, input().split())
            tmp.append((p, e))
        MPE.append(tmp)

    ans = solve(N, MPE)
    print(ans)


main()


def naive():
    N = input()
    count = {}
