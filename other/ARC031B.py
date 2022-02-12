A = ["x" + input() + "x" for _ in range(10)]
A = ["x" * 12] + A + ["x" * 12]

island_count = 0
for i in range(1, 11):
    for j in range(1, 11):
        if A[i][j] == "o":
            island_count += 1

from collections import deque

for i in range(1, 11):
    for j in range(1, 11):
        if A[i][j] == "x":
            seen = {(i, j): True}
            q = deque()
            q.append((i, j))
            while len(q):
                node = q.popleft()
                k, m = node
                neibors = [(k, m + 1), (k, m - 1), (k + 1, m), (k - 1, m)]
                for neibor in neibors:
                    if A[neibor[0]][neibor[1]] == "o" and neibor not in seen:
                        q.append(neibor)
                        seen[neibor] = True
            if len(seen) > island_count:
                print("YES")
                exit()

print("NO")
