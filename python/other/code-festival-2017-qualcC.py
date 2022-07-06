S = input()
N = len(S)
l = 0
r = N - 1
ret = 0
while l <= r:
    if S[l] == S[r]:
        l += 1
        r -= 1
    elif S[l] == "x":
        l += 1
        ret += 1
    elif S[r] == "x":
        r -= 1
        ret += 1
    else:
        print(-1)
        exit()
print(ret)


"""
少なくとも、x以外の小文字の数が偶数じゃないといけない
真ん中に来るのは奇数でもいい
xを飛ばして回文になるかどうか
xを飛ばす回数が操作回数では
x同士だったら飛ばさなくていい
反転するケースある？ないんじゃない？実装しよう


"""
