N = int(input())
A = list(map(int, input().split()))

ret = [0] * N
for i in range(N - 1):
    if A[i] > A[i + 1]:
        ret[i] ^= 1
        ret[i + 1] ^= 1

print(*ret)


"""
株の売買問題

上げる時、下げるときをトリガに換金する
問題は最後

同じ時どうする？
経路圧縮しとくのが楽？

解説が天才すぎる

"""
