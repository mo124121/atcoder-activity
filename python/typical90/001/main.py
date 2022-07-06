def cuttable(A, M, K, L):
    pre = 0
    count = 0
    for a in A:
        if a >= pre + M:
            pre = a
            count += 1
    if count > K:
        return True
    elif count == K and L - pre >= M:
        return True
    else:
        return False


def solve(N: int, L: int, K: int, A: "List[int]"):
    left = 0
    right = L
    mid = (right + left) // 2
    while left != mid:
        if cuttable(A, mid, K, L):
            left = mid
        else:
            right = mid
        mid = (right + left) // 2
    print(mid)
    return


def main():
    N, L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))
    solve(N, L, K, A)


if __name__ == "__main__":
    main()
