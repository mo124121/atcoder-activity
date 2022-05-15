N = int(input())
seen = {}
ret_i = 0
ret_max = 0
for i in range(1, N + 1):
    S, T = input().split()
    T = int(T)
    if S not in seen:
        if T > ret_max:
            ret_max = T
            ret_i = i
    seen[S] = True

print(ret_i)
