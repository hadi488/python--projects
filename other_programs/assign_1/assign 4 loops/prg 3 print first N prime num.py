x = input("enter a number: ")
x = int(x)
count = 1
j = 2
while(count <= x):
    i = 2
    while (True):
        if j % i == 0 and j != 2:
            j += 1
            i = 2
            continue
        elif j == i+1 or j == 2:
            print(j, end=", ")
            break
        i = i+1
    count += 1
    j = j+1
