N, C = map(int, input().split())
a = [0] * N
c = [0] * N
b = [0] * N
s = []
for i in range(N):
    a, b, c = map(int, input().split())
    s.append((a - 1, c))
    s.append((b, -c))

s.sort()
pre_time = 0
pre_cost = 0
ret = 0
for i in range(len(s)):
    time, cost = s[i]
    if pre_cost < C:
        ret += pre_cost * (time - pre_time)
    else:
        ret += C * (time - pre_time)
    pre_cost += cost
    pre_time = time

print(ret)
