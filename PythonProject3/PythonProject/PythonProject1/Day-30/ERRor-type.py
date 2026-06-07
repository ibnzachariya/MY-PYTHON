#FileNotFound
# with open("a.txt") as file
# file.read

#KeyError
#a_diction = {"key": "value")
#value = a_diction["non_existent_key)

#IndexError
# fruit_list = ["apple", "banana", "cherry"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

#......CATCHING EXCEPTIONS......
# try: something that might cause an exception
# except: do this if there was an exception
# else: do this if there were no exceptions
# finally: do this no matter what happens

#      raise error
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be above 3 meters")
bmi = weight / height ** 2
print(bmi)