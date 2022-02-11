#!/usr/bin/env python3
H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]
used = [[False] * W for _ in range(H)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def rec(sx, sy, cx, cy):
    if sx == cx and sy == cy and used[cx][cy]:
        return 0

    used[cx][cy] = True
    ret = -10000
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nx < 0 or nx >= H or ny < 0 or ny >= W or c[nx][ny] == "#":
            continue
        if (sx != nx or sy != ny) and used[nx][ny]:
            continue
        ret = max(ret, rec(sx, sy, nx, ny) + 1)
    used[cx][cy] = False
    return ret


def main():
    ret = 0
    for i in range(H):
        for j in range(W):
            ret = max(ret, rec(i, j, i, j))

    if ret > 2:
        print(ret)
    else:
        print(-1)


if __name__ == "__main__":
    main()
