S = input()
T = int(input())

x = 0
y = 0
amb_count = 0

for c in S:
    if c == "L":
        x -= 1
    elif c == "R":
        x += 1
    elif c == "U":
        y += 1
    elif c == "D":
        y -= 1
    elif c == "?":
        amb_count += 1
dist = abs(x) + abs(y)

if T == 1:
    print(dist + amb_count)
else:
    if dist >= amb_count:
        print(dist - amb_count)
    else:
        print((dist - amb_count) % 2)


"""
とりあえず確定しているマンハッタン距離を算出
?の数を数えておく

1なら足す,2ならひく

"""
