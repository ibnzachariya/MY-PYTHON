# # replacing the scores with grades
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
# student_grades = {}
#
# # Loop through each key in the student_scores dictionary
# for student in student_scores:
#
#     # Get the value (student score) by using the key each time.
#     score = student_scores[student]
#
#     # Check what grade the score would get, then add it to student_grades
#     if score >= 91:
#         student_grades[student] = 'Outstanding'
#     elif score >= 81:
#         student_grades[student] = 'Exceeds Expectations'
#     elif score >= 71:
#         student_grades[student] = 'Acceptable'
#     else:
#         student_grades[student] = 'Fail'
#
# print(student_grades)

fruits = {
    'mango': "green", 'banana': "yellow",
}
fruit_grade = {}
fruits['apple'] = "red"

for fruit in fruits:
    grade = fruits[fruit]
    if grade == "green":
        fruit_grade[fruit] = 'Very good'
    elif grade == "yellow":
        fruit_grade[fruit] = 'Good'
    else:
        fruit_grade[fruit] = 'Ok'

print(fruit_grade)
