x = input("enter a number: ")
x = int(x)
i = 1
print("factors of", x, "are")
while(i <= x):
    if x % i == 0:
        print(i, end=", ")
    i += 1