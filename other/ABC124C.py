S = input()
ret = [0] * 2

for i, c in enumerate(S):
    ret[i % 2] += int(c == "0")
    ret[1 - i % 2] += int(c == "1")
print(min(ret))
