# # len(12345)
# print(len("Hello)"))
#
# #A function that lets us to check what type a data is: type
# print(type("Hello"))
# print(type(1234))
# print(type(2.34))
# print(type(False))

#conversion e.g ("123") which is a string can be converted into integer by:
print(int("123") + int("123"))
#but cant convert something like string of letters into integers
#That would give VALUE ERRORS
int()
float()
str()
int()
bool()

#print("Number of letters in your name: " + str"len(input("Enter your name")))
name_of_the_user = input("Enter your name: ")
length_of_the_name = len(name_of_the_user)
print("Number of letters in your name: " + str(length_of_the_name))