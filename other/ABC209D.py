N, Q = map(int, input().split())
a = [0] * (N - 1)
b = [0] * (N - 1)
c = [0] * Q
d = [0] * Q

from collections import defaultdict,deque

G=defaultdict(list)

for i in range(N - 1):
    a[i], b[i] = map(int, input().split())
    G[a[i]].append(b[i])
    G[b[i]].append(a[i])

bin=[0]*(N+1)

st=deque()
st.append(1)
bin={1:0}
while len(st):
    node=st.pop()
    for neibor in G[node]:
        if neibor not in bin:
            bin[neibor]=(bin[node]+1)%2
            st.append(neibor)


ret=[]*Q
for i in range(Q):
    c, d = map(int, input().split())
    if bin[c]==bin[d]:
        ret.append("Town")
    else :
        ret.append("Road")

print(*ret,sep="\n")