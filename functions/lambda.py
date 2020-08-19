# def mul_me(num1, num2):
#     return num1 *num2
# print(mul_me(9,6))



mul_me = lambda *num: num[0] * num[1] * num [2]

print(mul_me(9,5,9,3,6,3,25,52))
