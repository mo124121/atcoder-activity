N = int(input())
c_true = 1
c_false = 1
for i in range(N):
    S = input()
    if S == "AND":
        c_false = 2 * c_false + c_true
    else:
        c_true = c_false + 2 * c_true


print(c_true)
