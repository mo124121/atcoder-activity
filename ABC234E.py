x = int(input())

def gen_candidate():
    candidate=[]
    for i in range(1,10):
        for j in range(-9,9):
            digit=i
            temp=""
            for k in range(18):
                temp+=str(digit)
                candidate.append(int(temp))
                digit+=j
                if not (0<=digit<=9):
                    break
    candidate.sort()
    return candidate

import bisect

cand=gen_candidate()

print(cand[bisect.bisect_left(cand,x)])