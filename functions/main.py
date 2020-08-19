from ali_module import *


num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

print("The number you have entered is num1: {} and num2: {}. Please read the below instructions to perform action".format(num1,num2))

print("Enter 1 for add, 2 for sub, 3 for mul, 4 for div and 5 for rem")
val = int(input("Enter your option: "))

if val==1:
    print(ali_module.add(num1,num2))

elif val==2:
    print(ali_module.sub(num1,num2))

elif val==3:
    print(ali_module.mul(num1,num2))

elif val==4:
    print(ali_module.div(num1,num2))

elif val==5:
    print(ali_module.rem(num1,num2))

else:
    print("The value entered {} is outside the boundary [1-5]".format(val))
    print()
