y = int(input())
m = int(input())
d = int(input())


def days(y, m, d):
    if m <= 2:
        m += 12
        y -= 1
    return 365 * y + y // 4 - y // 100 + y // 400 + (306 * (m + 1)) // 10 + d - 429


print(days(2014, 5, 17) - days(y, m, d))
