H, W = map(int, input().split())

MAP = [list(input()) for _ in range(H)]

import queue

def print_map():
    for i in range(len(MAP)):
        print(*(MAP[i]))

def solve():
    q = queue.Queue()
    for i in range(H):
        for j in range(W):
            if MAP[i][j] == "s":
                q.put((i,j))
                break

    while not q.empty():
        i,j =q.get()
        if (0<=i<H) and (0<=j<W):
            if MAP[i][j]=="g":
                return "Yes"
            elif MAP[i][j]!="#":
                MAP[i][j]="#"
                q.put((i+1,j))
                q.put((i-1,j))
                q.put((i,j+1))
                q.put((i,j-1))
            else:
                pass
    return "No"

print(solve())