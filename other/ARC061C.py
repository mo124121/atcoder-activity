S = input()

def sol1(s):
    import itertools
    ret = 0
    for pattern in itertools.product([False,True], repeat=len(s)-1):
        pre = 0
        for i in range(len(pattern)):
            if pattern[i]:
                ret+=int(s[pre:i+1])
                pre=i+1
        ret+=int(s[pre:])
    return ret

print(sol1(S))