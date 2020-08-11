print("If else condition for rating system")

# 0 = worst service
# 5 =  best service

feedback_score = int(input(" Please Enter your feed back either 0 or 5:"))

print(" The number you have entered is "+ str(feedback_score) + " as your feedback number")

if feedback_score == 0:
    print("Can you help us as the")
else:
    print("Thanks for your feedback")