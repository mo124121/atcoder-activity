x,y = input().split()

if x==y:
    print(x)
else:
    d = {"0":"","1":"","2":""}
    d.pop(x)
    d.pop(y)
    print(list(d.keys())[0])