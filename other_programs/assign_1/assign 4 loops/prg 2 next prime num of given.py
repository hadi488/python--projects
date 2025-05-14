x = input("enter a number: ")
x = int(x)
i = 2
while(i < x):
    if x % i == 0:
        print("not prime")
        break
    i += 1
else:
    j = i + 1
    i = 2
    while (True):
        if j % i == 0:
            j += 1
            i = 2
            continue
        elif j == i+1:
            print("next prime num is", j)
            break
        i += 1
