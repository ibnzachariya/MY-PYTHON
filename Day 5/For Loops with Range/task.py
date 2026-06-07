# for score in range(1, 10, 5):
#      print(score)
#
total = 0
for number in range(1, 101):
    total += number
print(total)
# for age in range(10, 20 and 20, 30):
#     print(age)

# def check_status(status):
#     if status.lower() == "faulty":
#         return "faulty"
#     else:
#         return "working"
#
#
# num_equipment = int(input("How many equipment do you want to check? "))
#
# faulty_count = 0
# working_count = 0
#
# for i in range(1, num_equipment + 1):
#     name = input(f"Enter name of equipment {i}: ")
#     status = input(f"Enter status of {name} (ok/faulty): ")
#
#     result = check_status(status)
#
#     if result == "faulty":
#         faulty_count += 1
#         if faulty_count > 3:
#             print("contact the technician immediately")
#     else:
#         working_count += 1
#
# print(f"Inspection complete: {faulty_count} faulty, {working_count} working")
