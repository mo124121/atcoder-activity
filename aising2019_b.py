N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))

Q = [0] * 3

for p in P:
    if p <= A:
        Q[0] += 1
    elif p <= B:
        Q[1] += 1
    else:
        Q[2] += 1

print(min(Q))
