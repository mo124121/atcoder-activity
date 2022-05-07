N, X, M = map(int, input().split())

A = [X]
seen = set()
seen.add(X)
for i in range(M):
    X = X**2 % M
    if X in seen:
        break
    seen.add(X)
    A.append(X)
in_index = A.index(X)
if in_index >= N:
    print(sum(A[:N]))
else:
    A_in = A[:in_index]
    A_loop = A[in_index:]
    in_sum = sum(A[:in_index])
    loop_sum = (N - in_index) // len(A_loop) * sum(A_loop)
    end_sum = sum(A_loop[: (N - in_index) % len(A_loop)])
    print(in_sum + loop_sum + end_sum)

"""
事前に数列を計算して、
後で合算すればよさそう
N<10**10
なんでもない

それでもM回の中に何回出てくるか数えればよろしい

あーループに入るやつがいるわ

"""
