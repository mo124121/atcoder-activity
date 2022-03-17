A, B = map(int, input().split())
ret = 0
count = 1
while count < B:
    ret += 1
    count += A - 1
print(ret)
