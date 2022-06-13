S = input()
N = len(S)
g_count = [0] * (N + 1)

for i, c in enumerate(S):
    g_count[i + 1] = g_count[i] + (-1) ** int(c != "g")

print(g_count[-1] // 2)
