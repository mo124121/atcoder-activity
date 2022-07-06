C = int(input())

M = [0] * C
N = [0] * C
L = [0] * C

for i in range(C):
    c = list(map(int, input().split()))
    c.sort()
    M[i], N[i], L[i] = tuple(c)

print(max(M) * max(N) * max(L))

"""
似たような問題みたことがある、けど解けた記憶がない
あれはサイズの決まった箱がいくつかある感じだったかつ向きは変えられない


向きを変えていい・・・がそれが厄介

向きをかえないならそれぞれのmax

各辺を高い順にソートしてmaxとればいいんじゃね？
sampleは通ったが、コーナーケースは存在しないか？
なかった
"""
