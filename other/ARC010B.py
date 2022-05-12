from collections import Counter


M = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}
M_DAYS = {1: 0}

for i in range(2, 13):
    M_DAYS[i] = M_DAYS[i - 1] + M[i - 1]


def solve(holidays):
    days = [False] * 367
    for i in range(1, 367):
        if i % 7 < 2:
            days[i] = True

    for holiday in holidays:
        while holiday < 367 and days[holiday]:
            holiday += 1
        if holiday < 367:
            days[holiday] = True
    r = 0
    ans = 0
    for d in days:
        if d:
            r += 1
        else:
            ans = max(ans, r)
            r = 0
    ans = max(ans, r)

    return ans


def main():
    N = int(input())
    holidays = []
    for i in range(N):
        m, d = map(int, input().split("/"))
        holidays.append(M_DAYS[m] + d)
    holidays.sort()
    ans = solve(holidays)
    print(ans)


main()

test = [[316] * 50]

for t in test:
    solve(t)
