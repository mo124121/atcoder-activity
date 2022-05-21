from decimal import ROUND_HALF_UP, Decimal


S = input()
X = Decimal(S).quantize(Decimal("0"), rounding=ROUND_HALF_UP)

print(X)
