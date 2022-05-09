X = list(input())


st = [X[0]]
for c in X[1:]:
    st.append(c)
    while len(st) > 1:
        if st[-2] == "S" and st[-1] == "T":
            st.pop()
            st.pop()
        else:
            break

print(len(st))

"""
普通にreplaceしたら怒られる？
あーまんなか消したらSTが現れる可能性があるのか
文字を追加しつつ、stackで消しこんでいく
"""
