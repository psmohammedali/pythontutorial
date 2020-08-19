for i in range(0,20):
    print("before > conditon")
    if i > 20:
        print("{} greater than 10".format(i))
        break
else:
    print("no value is printed")
