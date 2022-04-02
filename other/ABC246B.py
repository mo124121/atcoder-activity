A, B = map(int, input().split())

d = A**2 + B**2

print("{:.7f} {:.7f}".format((A**2 / d) ** 0.5, (B**2 / d) ** 0.5))
