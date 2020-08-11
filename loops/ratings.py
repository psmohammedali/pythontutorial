print("Rating system")

# user_number = int(input("Enter your feedback number between 1- 5: "))
#
# if user_number ==1:
#     print("We are sorry")
#
# elif user_number ==2:
#     print("We need to improve")
#
# elif user_number ==3:
#     print("Thanks")
#
# elif user_number == 4:
#     print("THank you so much")
#
# elif user_number ==5:
#     print("We are proud of ourself")
#
# else:
#     print("Please enter your rating between 1 - 5")


user_number = int(input("Enter your feedback number between 1- 5: "))

if user_number !=0 and user_number < 2:
    print("We are sorry")

elif user_number < 1 and user_number < 3:
    print("We need to improve")

elif user_number >2 and user_number < 4:
    print("Thanks")

elif user_number >3 and user_number <5:
    print("THank you so much")

elif user_number >4 and user_number == 5:
    print("We are proud of ourself")

else:
    print("Please enter your rating between 1 - 5")