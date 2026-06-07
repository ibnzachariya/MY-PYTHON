# #programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
# empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}

# Edit an item in a dictionary
# => programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#
# # Create a dictionary of equipment and their status
# equipment_status = {
#     "Generator": "working",
#     "Water Pump": "faulty",
#     "Air Conditioner": "working",
#     "Tractor": "faulty",
#     "Freezer": "working"
# }
#
# # Loop through dictionary
#  for key in programming_dictionary:
#       print(key)   => this will print out the keys from the programming_dictionary
#       print(programming_dictionary[key]) => this will print the values i.e retrieve what is present in each key

# faulty_count = 0
# working_count = 0
#
# for name, status in equipment_status.items():
#     print(f"{name} is {status}")
#     if status == "faulty":
#         faulty_count += 1
#     else:
#         working_count += 1

#print(f"Inspection complete: {faulty_count} faulty, {working_count} working")

# adding keys and values to a dictionary:
students_registration = {"Uniform": "Given", "Textbooks": "Not Given", "Tools": "Loading"}
print(students_registration)
students_registration["Books"] = "You Buy"
print(students_registration)
students_registration["100"] = "No buy"
print(students_registration)