from collections import deque


def solve(H, W, rs, cs, rt, ct, S):
    q = deque()
    count = -1
    S[rs][cs] = 0
    q.append((rs, cs, count))

    direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while len(q):
        r, c, count = q.popleft()
        if r == rt and c == ct:
            print(count)
            exit()
        for d in direct:
            r_next, c_next = r, c
            r_next += d[0]
            c_next += d[1]
            while S[r_next][c_next] != "#":
                if S[r_next][c_next] != "." and S[r_next][c_next] < count + 1:
                    break
                S[r_next][c_next] = count + 1
                q.append((r_next, c_next, count + 1))
                r_next += d[0]
                c_next += d[1]
    print("error")


def main():
    H, W = map(int, input().split())
    rs, cs = map(int, input().split())
    rt, ct = map(int, input().split())
    S = [list("#" + input() + "#") for _ in range(H)]
    S = [list("#" * (W + 2))] + S + [list("#" * (W + 2))]
    print(solve(H, W, rs, cs, rt, ct, S))


if __name__ == "__main__":
    main()
