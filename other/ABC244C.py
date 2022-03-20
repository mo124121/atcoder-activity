N = int(input())
seen = {}
min_i = 1
for i in range(N):
    print(min_i)
    seen[min_i] = True
    t = int(input())
    seen[t] = True
    for j in range(min_i, 2 * N + 2):
        if j not in seen:
            min_i = j
            break
print(min_i)
input()
