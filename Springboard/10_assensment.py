for i in range(1,6):
    for j in range(1,6):
        if (i % j != 0):
            pass
        elif j < i:
            continue
        else:
            print(i * j)