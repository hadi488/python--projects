x = input("enter start number: ")
y = input("enter end number: ")

x = int(x)
y = int(y)
j = x
while(x <= y):
    i = 2
    while (j <= y):
        if j % i == 0 and j != 2:
            j += 1
            i = 2
            continue
        elif j == i+1 or j == 2:
            print(j, end=", ")
            break
        i = i+1
    x +=1
    if j >= y :
        break
    j = j+1
