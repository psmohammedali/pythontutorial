#print('Prime number')


# todo write a program for finding a prime number

# userNum = int(input("Enter the number: "))
# print("The number you have entered is {}".format(userNum))
upper = int(input("Upper: "))
lower = int(input("Lower: "))

for userNum in range(lower,upper):
    if userNum==1:
        print("{} is prime or prime number".format(userNum))
    elif userNum>1:
        for i in range(2,userNum):
            if(userNum%i == 0):
                print(i)
                break
        else:
            print(userNum)

