N, L = map(int, input().split())
A = [input() for _ in range(L)]
B = input()
s = B.find("o")

for i in range(L):
    l = A[-1 - i]
    if s > 0 and l[s - 1] == "-":
        s -= 2
    elif s + 1 < 2 * N - 1 and l[s + 1] == "-":
        s += 2
print(s // 2 + 1)

"""
読むのが面倒だが、ただやるだけ

"""
