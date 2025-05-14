# x = input("enter a number: ")
# x = int(x)
# org = x
# remain = 0
# sum = 0
# count = len(str(x))
# mul = 0
# print("count is ", count)
# x = org
# while(x > 0):
#     remain = x % 10
#     x = x//10
#     mul = remain**count
#     sum = sum + mul
#     print(sum)
# if (sum== org):
#     print("armstrong number")
# else:
#     print("not armstrong number")





x = input("enter a number: ")
x = int(x)
org = x
sum = 0
num = str(x)
count = len(str(x))
print("count is ", count)
for dig in num:
    sum = sum + int(dig)**count
    print(sum)
if (sum == org):
    print("armstrong number")
else:
    print("not armstrong number")





# x = input("enter a number: ")
# x = int(x)
# org = x
# remain = 0
# sum = 0
# count = len(str(x))
# mul = 0
# print("count is ", count)
# for i in range(1,count+1):
#     remain = x % 10
#     x = x // 10
#     mul = remain ** count
#     sum = sum + mul
#     print(sum)
# if (sum == org):
#     print("armstrong number")
# else:
#     print("not armstrong number")
