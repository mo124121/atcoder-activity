N = int(input())

for k in range(1, N + 1):
    if k * (k + 1) // 2 == N:
        print("Yes")
        print(k + 1)
        ret = [[] for _ in range(k + 1)]
        edge_i = 1
        for i in range(k + 1):
            for j in range(i):
                ret[i].append(edge_i)
                ret[j].append(edge_i)
                edge_i += 1
        for line in ret:
            print(len(line), *line)

        exit()
    elif k * (k + 1) // 2 > N:
        break

print("No")


"""
3

12
 23
1 3

6
123
  345
1   56
 2 4 6

10
1234
   4567
1     789
 2  5  8 A
  3  6  9A

15
12345
    56789
1       9ABC
 2   6   A  DE
  3   7   B D F
   4   8   C EF


123456
     6789AB
1         BCDEF
 2    7    C   GHI
  3    8    D  G  JK
   4    9    E  H J L
    5    A    F  I KL


解の形態はわかるが、きれいな実装がわからない

解説読んだ、天才すぎる

逆三角形のイメージを持つこと面白い

別解の完全グラフはとても面白い
"""
