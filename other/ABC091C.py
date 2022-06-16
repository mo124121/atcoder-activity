N = int(input())
AB = []
for i in range(N):
    AB.append(tuple(map(int, input().split())))
AB.sort(key=lambda x: x[1])
CD = []
for i in range(N):
    CD.append(tuple(map(int, input().split())))
CD.sort()

ret = 0
red = []
blue = []

for c, d in CD:
    max_i = -1
    max_y = -1
    for i, (a, b) in enumerate(AB):
        if a < c and b < d:
            if max_y < b:
                max_i = i
                max_y = b
    if max_i != -1:
        del AB[max_i]
        ret += 1
print(ret)


"""
マッチングの問題っぽいがその手の知識はない

青の内側に赤があるイメージ


N<=100で小さい
N**4

貪欲になるべく大きい赤を青に埋めていく、的な？
類題見た気がするなあ

AC

解説後
やっぱり2部最大マッチングだし覚え解くべき問題

"""
