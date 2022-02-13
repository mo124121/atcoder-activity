from collections import defaultdict


N, A = map(int, input().split())
x = list(map(int, input().split()))

y = [z - A for z in x]

y.sort()

occurence = defaultdict(int)
for z in y:
    occurence[z] += 1

minus_occ = defaultdict(int)
minus_occ[0] = 1
plus_occ = defaultdict(int)
plus_occ[0] = 1

for z in y:
    if z < 0:
        temp = defaultdict(int)
        for mkey, mvalue in minus_occ.items():
            temp[mkey + z] += mvalue
        for mkey, mvalue in temp.items():
            minus_occ[mkey] += mvalue

    if z > 0:
        temp = defaultdict(int)
        for pkey, pvalue in plus_occ.items():
            temp[pkey + z] += pvalue
        for pkey, pvalue in temp.items():
            plus_occ[pkey] += pvalue

if occurence[0] == 0:
    ret = 0
    pat = 1
else:
    ret = 2 ** occurence[0] - 1
    pat = 2 ** occurence[0]

for key, value in minus_occ.items():
    if -key in plus_occ and key != 0:
        ret += value * plus_occ[-key] * pat
print(ret)
