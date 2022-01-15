from functools import lru_cache

@lru_cache(maxsize=None)
def rec(left:int,right:int):
    if right == 0:
        return [""]
    if left==right:
        return ["("+s for s in rec(left-1,right)]
    elif left==0:
        return [")"+s for s in rec(left,right-1)]
    else:
        return ["("+s for s in rec(left-1,right)]+[")"+s for s in rec(left,right-1)]

def main():
    N =int(input())
    
    if N%2!=0:
        return
    else:
        ret=rec(N//2,N//2)
        print(*ret,sep="\n")
        return

main()
