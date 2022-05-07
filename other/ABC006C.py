N, M = map(int, input().split())

if M < 2 * N or 4 * N < M:
    print(-1, -1, -1)
    exit()
M -= 2 * N
baby = M // 2
eld = M - baby * 2
adult = N - baby - eld
print(adult, eld, baby)
# print(adult * 2 + eld * 3 + baby * 4)
"""
見るからにdp

そうでもない？

とりあえずM-2*Nして考えるほうが楽そう
だめなケースはM<2*N,4*N<M

"""
