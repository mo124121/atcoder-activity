N, H = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

base_a = max(A)
B.sort()

ret = 0
while len(B):
    b = B.pop()
    if b <= base_a:
        break
    if H <= 0:
        break
    H -= b
    ret += 1
if H > 0:
    ret += (H + base_a - 1) // base_a

print(ret)

"""
繰り返し振るのはmax(a)でいい
逆にこれ以外は即投げていい、ただ,max(a)未満のものは不要
あとはシミュレーションしたらいいと思う
heapqぐらい使うか

1WAつらい
コーナーケース

実装整理
1WA...

H<=0のゾンビがおった、AC


"""
