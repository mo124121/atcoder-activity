s = input()
t = input()

def func():
    hoge=s
    if s==t:
        return 0

    for i in range(len(s)):
        hoge=hoge[-1]+hoge[:-1]
        if hoge==t:
            return i+1
    
    return -1

print(func())