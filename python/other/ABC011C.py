N = int(input())
a = [int(input()) for _ in range(3)]
a.sort()
if N in a:
    print("NO")
    exit()

for i in range(100):
    for j in range(3, 0, -1):
        if N - j not in a and N - j >= 0:
            N -= j
            break

if N == 0:
    print("YES")
else:
    print("NO")

"""
考察
連続してなかったらいい、すり抜けられる

問題文見逃し
100回しか引けない

愚直にすべき
"""
