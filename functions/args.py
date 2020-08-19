def Two_add(*num):
    total = 0
    length = len(num)
    if len(num) <=2:
        print(len(num))
        for i in num:
            total = total + i
        print(total)
        print("Hello")
    # return total
    else:
        print("the number of arguments you have enter is {}".format(length))

Two_add(5,6,11)

