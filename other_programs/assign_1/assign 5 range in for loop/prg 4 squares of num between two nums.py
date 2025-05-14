x = input("enter first number: ")
y = input("enter last number: ")

x = int(x)
y = int(y)
print("square of nums is")
for i in range(x, y+1):
    print(i*i, end=",")