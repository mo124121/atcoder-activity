N=int(input())

x_origin=0
y_origin=0
t_origin=0
ret="Yes"
for i in range(N):
    t_target, x_target, y_target = map(int,input().split())
    diff_x = x_target-x_origin
    diff_y = y_target-y_origin
    steps = abs(diff_x)+abs(diff_y)
    t_spent = t_target-t_origin
    if steps>t_spent:
        #print("too far")
        ret="No"
    elif (steps-t_spent)%2 != 0:
        #print("near!")
        #print(f"{t_origin=} {x_origin=} {y_origin=} -> {t_target=} {x_target=} {y_target=}")
        ret="No"
    else:
        t_origin = t_target
        x_origin = x_target
        y_origin = y_target

print(ret)