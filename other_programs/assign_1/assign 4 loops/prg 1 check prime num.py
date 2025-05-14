# x = input("enter a number: ")
# x = int(x)
# i = 2
# while(i < x):
#     if x % i == 0:
#         print("not prime")
#         break
#     i += 1
# else:
#     print("prime")



x = input("enter a number: ")
x = int(x)
i = 2
while(i < x):
    if x % i == 0:
        print("not prime")
        break
    i += 1
if i  == x:
    print("prime")