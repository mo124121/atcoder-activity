from bisect import bisect, bisect_left


N = int(input())
W = [int(input()) for _ in range(N)]

box = []

for w in W:
    i = bisect_left(box, w)
    if i == len(box):
        box.append(w)
    else:
        box[i] = w
    box.sort()

print(len(box))
