N = int(input())
X = list(map(int, input().split()))

m = j = c = 0
for x in X:
    m += abs(x)
    j += x**2
    c = max(c, abs(x))

print(f"{m}")
print(f"{j**0.5:.10f}")
print(f"{c}")
