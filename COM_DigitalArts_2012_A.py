s = input()
N = int(input())

t=[0]*N
for i in range(N):
    t[i]=input()
    
ret=[]
for word in s.split():
    same_flag=False
    for ng_word in t:
        if len(word)!=len(ng_word):
            continue
        same_flag_in=True
        for c_in,c_ng in zip(word,ng_word):
            if c_ng =="*":
                continue
            else:
                if c_in != c_ng:
                    same_flag_in=False
                    break
        if same_flag_in:
            same_flag=True
            break
            
    
    if same_flag:
        ret.append("".join("*"*len(word)))
    else:
        ret.append(word)
    
print(" ".join(ret))