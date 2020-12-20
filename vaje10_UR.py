import math
# num = int(input("Please, enter a number."))

for j in range (2, 100):
    until = int(math.sqrt(j))
    res = False

    for i in range(2, until+1):
        if j % i == 0:
            res = True
            break

    if res == False:
        print(j)
