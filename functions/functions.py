print("Discussion on functions")

# def welcome():
#     print("Welcome")
#     return


# def greet(user):
#     print("welcome {}, Nice to meet you".format(user))
#     print("welcome {}, Nice to meet you".format(user))
#     print("welcome {}, Nice to meet you".format(user))
#     return
#     print("welcome {}, Nice to meet you".format(user))
#
#
# greet("Ali")


Name = input("Enter your name buddy: ")
Age  = int(input("Enter your current Age: "))
Gender = (input("Enter your gender (F (or) M (or) T: "))[0]

def summary(a,b,c):
    print("Your Name is {} and your age is {} and your gender is {}".format(a, b, c))
    return

summary(Name, Age, Gender)
