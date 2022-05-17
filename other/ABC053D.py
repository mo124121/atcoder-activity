from collections import Counter


N = int(input())
A = list(map(int, input().split()))

count = Counter(A)
ret = 0
c = 0
for v in count.values():
    if v != 1:
        c += v - 1
    ret += 1
print(ret - c % 2)


"""
なんにせよ2個以上あるのを候補に消していく感じ



"""
