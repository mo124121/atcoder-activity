N = int(input())
S = [input()[::-1] for _ in range(N)]
S.sort()

for s in S:
    print(s[::-1])
