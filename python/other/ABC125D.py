N = int(input())
A = list(map(int, input().split()))

m_count = sum(int(a < 0) for a in A)
abs_min = min(abs(a) for a in A)
ret = sum(abs(a) for a in A)

if m_count % 2:
    ret -= abs_min * 2

print(ret)
