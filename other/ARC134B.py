N = int(input())
S = [*input()]
a_ascii = ord("a")
left = 0
right = N - 1
for i in range(26):
    target = chr(a_ascii + i)
    curr_left = left
    curr_right = right
    while curr_left < curr_right:
        if S[curr_left] > target:
            while curr_left < curr_right:
                if S[curr_right] == target:
                    S[curr_left], S[curr_right] = (
                        S[curr_right],
                        S[curr_left],
                    )
                    curr_left += 1
                    curr_right -= 1
                    left, right = curr_left, curr_right
                    break
                else:
                    curr_right -= 1
        else:
            curr_left += 1

print(*S, sep="")
