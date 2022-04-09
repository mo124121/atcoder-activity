N = int(input())
A = list(map(int, input().split()))

l = 0
r = N - 1
rev = 0

while l <= r:
    if A[r] == rev:
        r -= 1
        continue

    if A[l] != rev:
        print("No")
        exit()
    else:
        l += 1
        rev = 1 - rev
print("Yes")


"""
考察
N<2*10**5
O(NlogN)あたりまで

操作Aは1との排他的論理和 ^

連続した数値を入れたかったらBを使う
反転させたかったらAを使う
0101を作りたいなら前半側で->必ずしもそうではない

逆からやれば消せるはず
後ろ優先で操作→できないときは前、とか？
"""
