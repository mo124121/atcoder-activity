N = int(input())
S = input()

st = []
for c in S:
    st.append(c)
    if st[-3:] == list("fox"):
        for _ in range(3):
            st.pop()

print(len(st))
