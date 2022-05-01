from collections import deque


H, W = map(int, input().split())

S = (
    [["#"] * (W + 2)]
    + [["#"] + list(input()) + ["#"] for _ in range(H)]
    + [["#"] * (W + 2)]
)
ret = 0
q = deque()
mvs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for sh in range(1, H + 1):
    for sw in range(1, W + 1):
        if S[sh][sw] == "#":
            continue
        q.append((sh, sw, 0))
        seen = set()
        seen.add((sh, sw))
        while len(q):
            h, w, c = q.popleft()
            for mv in mvs:
                nh = h + mv[0]
                nw = w + mv[1]
                if S[nh][nw] == "." and (nh, nw) not in seen:
                    q.append((nh, nw, c + 1))
                    seen.add((nh, nw))
        ret = max(ret, c)
print(ret)

"""
H,W<20

幅探索を全てのスタートでして、一番遠いところを更新していく
HW*HW

"""
