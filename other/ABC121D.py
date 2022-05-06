A, B = map(int, input().split())
ret = 0
for i in range(A, B + 1):
    ret ^= i
    print(bin(i), bin(ret))
"""
直感的に端だけみればいい気がする
いったんシミュレーションだけしてみる
桁が上がる毎にリセットされるように見える

まあ、ある桁のbitが何回立つか問題

"""
