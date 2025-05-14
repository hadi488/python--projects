num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
num3 = int(input("enter third number : "))
# if num1 > num2:
#     if num1 > num3 :
#         print("first num {} is greater".format(num1))
# if num2 > num1:
#     if num2 > num3 :
#         print("2nd num {} is greater".format(num2))
# if num3 > num1:
#     if num3 > num2:
#         print("3rd num {} is greater".format(num3))

if num1 > num2:
    if num1 > num3:
        print("first num {} is greater".format(num1))
    else:
        print("3rd num {} is greater".format(num3))
elif num2 > num1:
    if num2 > num3:
        print("2nd num {} is greater".format(num2))
    else:
        print("3rd num {} is greater".format(num3))



