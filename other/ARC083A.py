A, B, C, D, E, F = map(int, input().split())

highest = 0
water_h = A * 100
sugar_h = 0

for ai in range(F // (100 * A) + 1):
    for bi in range(F // (B * 100) + 1):
        water_total = ai * A + bi * B
        for ci in range(F // C + 1):
            sugar_c = C * ci
            for di in range(F // D + 1):
                sugar_total = D * di + sugar_c
                if water_total * 100 + sugar_total > F:
                    break
                if E * (A * ai + B * bi) >= (C * ci + D * di):
                    if sugar_total + water_total:
                        concentration = (
                            100 * (sugar_total) / (sugar_total + 100 * water_total)
                        )
                    else:
                        concentration = 0
                    if highest < concentration:
                        highest = concentration
                        water_h = water_total * 100
                        sugar_h = sugar_total
print(water_h + sugar_h, sugar_h)
