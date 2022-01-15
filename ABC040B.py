n = int(input())

import math
width = int(math.ceil(math.sqrt(n)))

ret =100000
for w in range(1,1+width):
    buf = abs(w- n//w)+n%w
    if ret>buf:
        ret=buf

print(ret)