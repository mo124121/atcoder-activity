N = int(input())
hist = [0] * (2 * 10**5 + 1)
MOD = 10**9 + 7
prev = 0
hist[0] = 1

for i in range(N):
    c = int(input())
    if c == prev:
        continue
    count = 0
    count = (hist[prev] + hist[c]) % MOD
    hist[c] = count
    prev = c

print(hist[prev])
