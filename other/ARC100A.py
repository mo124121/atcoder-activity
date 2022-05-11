N = int(input())
A = list(map(int, input().split()))
B = [A[i] - i - 1 for i in range(N)]
B_sum = sum(B)
ret = 0
shift = B_sum // N
for b in B:
    ret += abs(b - shift)

ret2 = 0
if B_sum > 0:
    shift += 1
else:
    shift -= 1
for b in B:
    ret2 += abs(b - shift)

print(min(ret, ret2))


"""
数列全体をシフトするイメージ

左右へのずれ量を合算していく？
とりあえず黙って1...Nは引いたほうがわかりやすいのでは？

この状態で合計を計算し、Nの倍数を足し引きして0にもっとも近くなる時の悲しみ

6WA/19

2分法のほうが筋がいいか？
単調増加じゃないから無理

左側にある数と右側にある数が同一になるのが答え
Bをソートして、-B[N//2]を全体にすればいい、ほんまか？


"""
