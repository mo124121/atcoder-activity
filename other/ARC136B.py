N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def No():
    print("No")
    exit()


if sorted(A) != sorted(B):
    No()

if len(set(A)) == N:
    cnt = 0
    for i in range(N):
        cnt += A.index(B[i])
        A.remove(B[i])
    if cnt % 2 == 0:
        print("Yes")
    else:
        No()
else:
    print("Yes")
