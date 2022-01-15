K=int(input())

ret = bin(K)[2:]
ret=ret.replace("1","2")
print(ret)