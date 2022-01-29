def func_28157592():
    from collections import deque
    N = int(input())
    S = input()
    T = input()
    a = deque()
    b = deque()
    ans = 0
    for i in range(N):
        if T[i] == "1":
            b.append(i)
        if S[i] == "1":
            if a:
                ans += i - a.popleft()
            elif b:
                ans += i - b.popleft()
            else:
                a.append(i)
    if a or b:
        print(-1)
    else:
        print(ans)

func_28157592()

#sugee