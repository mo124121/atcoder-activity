N =int(input())
V = list(map(int,input().split()))

V.sort()

ret = V[0]

for v in V[1:]:
    ret=(ret+v)/2
print("{:.5f}".format(ret))