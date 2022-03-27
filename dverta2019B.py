R, G, B, N = map(int, input().split())
ret = 0
for r in range(N // R + 1):
    N_r = N - r * R
    for g in range(N_r // G + 1):
        N_b = N - r * R - g * G
        if N_b >= 0 and N_b % B == 0:
            ret += 1

print(ret)
