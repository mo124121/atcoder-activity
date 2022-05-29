from array import array
from bisect import bisect_left, bisect_right, insort

Q = int(input())
S = array("i")

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        insort(S, q[1])
    elif q[0] == 2:
        r = bisect_right(S, q[1])
        l = bisect_left(S, q[1])
        c = r - l
        if c != 0:
            del S[l : l + min(c, q[2])]
    else:
        print(S[-1] - S[0])
