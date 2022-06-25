def solve(N, K):
    size = 1
    count = 1
    for i in range(N):
        size = size * 2 + 3
        count = count * 2 + 1
    ret = 0
    for i in range(N + 1):
        if K == size:
            ret += count
            break
        if K == 1:
            break

        size = (size - 3) // 2
        count = (count - 1) // 2
        if K == size + 2:
            ret += count + 1
            break
        elif K > size + 2:
            ret += count + 1
            K -= size + 2
        else:
            K -= 1

    return ret


def main():
    N, K = map(int, input().split())
    ret = solve(N, K)
    print(ret)


def naive(N, K):
    burger = "P"
    for _ in range(N):
        burger = "B" + burger + "P" + burger + "B"
    ret = 0
    for c in burger[:K]:
        if c == "P":
            ret += 1
    return ret


main()

# n = 2
# s = 1
# for _ in range(n):
#     s = s * 2 + 3
# for i in range(s + 1):
#     sol = solve(n, i)
#     nai = naive(n, i)
#     if sol != nai:
#         print(n, i, sol, nai)
