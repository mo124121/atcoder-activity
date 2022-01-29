N = input()

digit_sum = 0
for d in N:
    digit_sum += int(d)

if digit_sum % 9 == 0:
    print("Yes")
else:
    print("No")
