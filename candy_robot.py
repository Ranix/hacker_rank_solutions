n = 8
t = 6
c = [3, 1, 7, 5, 7, 4]
interaction = 1
bowl = n
total_fill = 0
for grab_candy in c:
    bowl = bowl - grab_candy
    print("bowl: " + str(bowl))
    if interaction == t:
        print(total_fill)
    else:
        if bowl < 5:
            fill = n - bowl
            total_fill += fill
            print("total: " + str(total_fill) )
            bowl += fill
            print("fill:" + str(fill))
    interaction += 1
