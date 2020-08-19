# myList1 = list(range(10))
# print(myList1)
#
# mystr = 10
#
#
#
# mylist2 = list(range())
# print(mylist2)

# myName = input("Enter your name: ")
# n = len(myName)
#
# #print(n)
#
# for i in range(n):
#     print(myName[i])
mylist1 = ["Mohammed","Kaviya","Monish","Srienath"]
mylist2 = ["Ali","Bhavana","Ayesha","Vidhya"]

# print(mylist1)
# print(mylist2)

final = mylist1 + mylist2
print(final)

mylist1.append(mylist2)
mylist1.extend(mylist1)
print(mylist1)