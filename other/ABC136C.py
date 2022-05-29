N = int(input())
H = [0] + list(map(int, input().split()))


def no():
    print("No")
    exit()


prev = 0
for i in range(N):
    if H[i] < H[i + 1]:
        H[i + 1] -= 1
    if H[i] > H[i + 1]:
        no()
print("Yes")
