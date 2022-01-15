N=int(input())
t_pre=0
x_pre=0
y_pre=0

ret="Yes"
for i in range(N):
    t, x, y = map(int, input().split())
    t_diff = t-t_pre
    x_diff = x-x_pre
    y_diff = y-y_pre
    if t_diff < abs(x_diff)+abs(y_diff):
        ret="No"
        break
    elif (t_diff + abs(x_diff)+abs(y_diff))%2!=0:
        ret="No"
        break
    else:
        t_pre=t
        x_pre=x
        y_pre=y
print(ret)