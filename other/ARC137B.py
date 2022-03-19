N = int(input())
A = list(map(int, input().split()))


max_zero = 0
max_one = 0

l = 0
while l < N:
    one_count = 0
    for r in range(l, N):
        if A[r] == 1:
            one_count += 1
            max_one = max(max_one, one_count)
        else:
            one_count -= 1
        if one_count <= 0:
            break
    l = r + 1
l = 0
while l < N:
    zero_count = 0
    for r in range(l, N):
        if A[r] == 0:
            zero_count += 1
            max_zero = max(max_zero, zero_count)
        else:
            zero_count -= 1
        if zero_count <= 0:
            break
    l = r + 1

print(max_zero + max_one + 1)


"""
全探索は始点N×終点N->O(N^2)

なんか始点と終点が逆転するイメージ?
01となった時点で幅が狭まる、それをカウントダウンする？
尺取り法っぽいがWAがちょろちょろ、どうする？


1111100000
1101100000
1100100000

0110   0 1 2 3 ->4
010101 2 3 4   ->3



"""
