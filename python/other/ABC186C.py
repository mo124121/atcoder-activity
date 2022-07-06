N= int(input())

def check10(x):
    for c in str(x):
        if c=="7":
            return False
    return True

def change_base(val,base):
    if(int(val/base)):
        return change_base(int(val/base),base)+str(val%base)
    return str(val%base)

def check8(x):
    x_8=change_base(x,8)

    for c in x_8:
        if c=="7":
            return False
    return True

count=0
for i in range(1,N+1):
    if check10(i)and check8(i):
        count+=1
    

print(count)