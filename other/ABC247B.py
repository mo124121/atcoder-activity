N = int(input())
S = [input().split() for i in range(N)]


for i in range(N):
    flag_s = False
    flag_t = False
    for j in range(N):
        if i == j:
            continue
        if S[i][0] == S[j][0] or S[i][0] == S[j][1]:
            flag_s = True
        if S[i][1] == S[j][0] or S[i][1] == S[j][1]:
            flag_t = True
    if flag_s and flag_t:
        print("No")
        exit()


print("Yes")
