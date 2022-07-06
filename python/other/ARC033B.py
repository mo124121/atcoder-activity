Na, Nb = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = set(A)
B = set(B)
C = A.intersection(B)
D = A.union(B)
print("{:.7f}".format(len(C) / len(D)))


"""
辞書に登録してカウントすればいい
おそらくA内orB内でも同じのが複数回出てくる可能性があるので
そこは注意する必要がある

黙ってsetにしたらいいのでは？

"""
