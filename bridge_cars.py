U = 9
weight = [3,4,5,7,4,7,2,9]
turnBacks = []
i = 0
j = 1
while i < len(weight):
    print(weight[i])
    if weight[i] > U:
        turnBacks.append(weight.pop(i))
        continue
    while i+j < len(weight):
        print(j)
        print(i)

        if weight[i] + weight[i+j] > U:
            turnBacks.append(weight.pop(i+j))
            print(weight)
        else:
            j = 1
            break

    i += 1
print(turnBacks)
