x = input("enter a number: ")
x = int(x)
i = 1
print(f"all prime factors of given num is")
while(i <= x):
    if x % i == 0:
        print("")
    elif j == i+1 or j == 2:
        print(j, end=", ")
        break
    i = i+1
    j = j+1
