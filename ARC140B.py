import re


N = int(input())
S = input()

counts = []

a_count = 0
A = "A"
R = "R"
C = "C"
stat = C


for pat in re.finditer("A+|R+|C+", S):
    l = pat.regs[0][1] - pat.regs[0][0]
    if S[pat.start()] == A:
        stat = A
        a_count = l
    elif S[pat.start()] == R:
        stat = R
        if l != 1:
            a_count = 0
    else:
        if stat == R and a_count > 0:
            counts.append(min(a_count, l))
        stat = C
        a_count = 0

ret = min(len(counts) * 2, sum(counts))

print(ret)
