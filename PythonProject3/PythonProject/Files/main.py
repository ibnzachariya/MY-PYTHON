#file = open("my_file.txt") OR
# with open("my_file.txt") as file: #with this method no need to add file.close() at the end
#     contents = file.read()
#     print(contents)

# if we wanted to access and replace the file,
with open("my_file.txt", mode="a") as file:
    file.write("\nNew something") #the w is to write new, if its "a",stands for append i e to add more texts










    #file.close() # => this tells stop accessing the file it has tapped into
