S = input()

if S == "a" or S == "z" * 20:  # 不可ケース
    print("NO")
elif len(S) == 1:  # 1文字
    print(chr(ord(S) - 1) + "a")
else:
    if S != S[::-1]:  # リバース
        print(S[::-1])
    else:
        h = sum(ord(c) - ord("a") + 1 for c in S)
        S2 = ""
        while h > 0:
            if h >= 26:
                S2 += "z"
                h -= 26
            else:
                S2 += chr(h - 1 + ord("a"))
                h = 0
        if S != S2:
            print(S2)
        else:
            print(S2[:-1] + "ya")
