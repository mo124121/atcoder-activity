B, C = map(int, input().split())

if C == 1:
    if B == 0:
        print(1)
    else:
        print(2)
    exit()

if B == 0:
    print(1 + C // 2 + (C - 1) // 2)
elif B > 0:
    if B - C // 2 <= -B + (C - 1) // 2:
        print(1 + B + (C - 2) // 2 + B + (C - 1) // 2)
    else:
        print(1 + (C - 2) // 2 + C // 2 + 1 + (C - 1) // 2 + (C - 1) // 2)
else:
    if -B - (C - 1) // 2 <= B + (C - 2) // 2:
        print(1 - B + (C - 1) // 2 - B + C // 2)
    else:
        print(1 + (C - 2) // 2 + C // 2 + 1 + (C - 1) // 2 + (C - 1) // 2)


"""
以前あかんかった、2度目

符号反転はやっても2回


10 10
5 6 7 8 9 10 11 12 13 14 
->  B-C//2 <= A <= B+(C-2)//2
-14 -13 -12 -11 -10 -9 -8 -7 -6 
-> -B-(C-1)//2 <= A <=-B+(C-1)//2

10 11
5 6 7 8 9 10 11 12 13 14
->  B-C//2 <= A <= B+(C-2)//2
-15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5
-> -B-(C-1)//2 <= A <= B+(C-1)//2

-10 10
-15 -14 -13 -12 -11 -10 -9 -8 -7 -6
B-C//2 <=A<=B+(C-2)//2
6 7 8 9 10 11 12 13 14 
-B-(C-1)//2 <=A<=B+(C-1)//2


AC これぐらいなら丁寧に場合分けでよい



"""
