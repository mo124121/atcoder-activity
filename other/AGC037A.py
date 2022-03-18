S = input()
seen = {}

K = 0
prev = ""
current = ""
history = []
for s in S:
    current += s
    if prev != current:
        history.append(current)
        prev = current
        current = ""
        K += 1
if current == prev:
    history[-1] += prev
print(len(history))
