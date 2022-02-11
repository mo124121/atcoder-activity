S = input()
N = len(S)
ret = [0] * N
st = 0
r = 1
while st < N:
    if S[r] == "L":
        l = r - 1
        end = r + 1
        while end < N:
            if S[end] == "R":
                break
            end += 1
        ret[r] = (r - st) // 2 + (end - 1 - l + 1) // 2
        ret[l] = (r - st + 1) // 2 + (end - 1 - l) // 2
        st = end
        r = st + 1
    else:
        r += 1

print(*ret)
