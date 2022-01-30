S = input()
YES = "Yes"
NO = "No"
pre_a_count = 0
for c in S:
    if c == "a":
        pre_a_count += 1
    else:
        break
if pre_a_count == len(S):
    print(YES)
    exit()

post_a_count = 0
for c in reversed(S):
    if c == "a":
        post_a_count += 1
    else:
        break
if pre_a_count > post_a_count:
    print(NO)
    exit()

left = pre_a_count
right = len(S) - post_a_count - 1

while left < right:
    if S[left] != S[right]:
        print(NO)
        exit()
    left += 1
    right -= 1
print(YES)
