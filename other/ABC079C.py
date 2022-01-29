s= input()

def dfs(ops):
    if 3==len(ops):
        total = int(s[0])
        ret=s[0]
        for j in range(len(ops)):
            ret+=ops[j]+s[j+1]
            if ops[j] =="+":
                total += int(s[j+1])
            elif ops[j]=="-":
                total -= int(s[j+1])

        if total==7:
            return ret+"=7"
        else:
            return None

    else:
        ret = dfs(ops+"+")
        if ret is not None:
            return ret
        ret = dfs(ops+"-")
        if ret is not None:
            return ret

print(dfs(""))