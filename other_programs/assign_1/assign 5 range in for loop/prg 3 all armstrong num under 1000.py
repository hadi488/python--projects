
for number in range(0,1000000001):
    sum = 0
    org = number
    # print("org = ",org, type(org))
    num = str(number)
    # print("num = ", num ,type(num))
    count = len(num)
    # print("count = ", count ,type(count))
    for dig in num:
        sum = sum + int(dig) ** count
        # print("dig = ", int(dig), type(int(dig)))
        # print(sum)
    if (sum == org):
        print(org, end=", ")




