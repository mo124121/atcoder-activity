N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

dp = [{} for _ in range(N + 1)]

multiply_list = []
for i in range(N):
    for j in range(N):
        if Q[j] % P[i] == 0:
            multiply_list.append((i, -j))

multiply_list.sort()

ret = 0
current_ret = 0
for i in range(len(multiply_list) - 1):
    if multiply_list[i] < multiply_list[i + 1]:
        current_ret += 1
    else:
        if ret < current_ret:
            ret = current_ret
        current_ret = 0

print(ret)
