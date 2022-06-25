N = int(input())
S = input()
W = list(map(int, input().split()))

SW = [(W[i], S[i]) for i in range(N)]
SW.sort()

count = sum(map(int, list(S)))
ret = count

wpre = 0
for w, s in SW:
    if wpre != w:
        ret = max(ret, count)
    wpre = w
    if s == "0":
        count += 1
    else:
        count -= 1

ret = max(ret, count)
print(ret)
