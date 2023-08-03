for i in range(1,6):
    for j in range(0,6-i):
        print(" ", end="")

    for k in reversed(range(1,i)):
        print(k, end="")

    print("")
