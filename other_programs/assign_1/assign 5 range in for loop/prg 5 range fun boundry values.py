x = input("enter first number: ")
y = input("enter last number: ")
step = input("enter step")

x = int(x)
y = int(y)
step = int(step)
print("nums are")
for i in range(x, y+1, step):
    print(i, end=",")