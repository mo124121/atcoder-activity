A, B, C, K = map(int, input().split())

if K % 2 == 0:
    print(A - B)
else:
    print(B - A)


"""
シミュレートすべき
A B C
BC CA AB
CAAB ABBC BCCA A+ABC B+ABC C+ABC ABC=Z
BCZZ CAZZ ABZZ
CAABZZZZ ABBCZZZZ BCCAZZZ ->A5Z B5Z C5Z
BC10Z 

結構早々にあふれるはずなので、
操作トレースでよさそう


あー差をとるのね？
であれば、シンプル　操作を繰り返してもA B C or B+C C+A A+Bの繰り返し
Kの偶奇をとればいい

"""
