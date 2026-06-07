# Basic Python Quiz Game

questions = [
    {"question": "What is the correct file extension for Python files?",
     "options": ["A. .py", "B. .python", "C. .pt", "D. .pyt"],
     "answer": "A"},

    {"question": "Which keyword is used to define a function in Python?",
     "options": ["A. func", "B. def", "C. function", "D. define"],
     "answer": "B"},

    {"question": "Which data type is used to store True or False values?",
     "options": ["A. int", "B. str", "C. bool", "D. float"],
     "answer": "C"},

    {"question": "What symbol is used for comments in Python?",
     "options": ["A. //", "B. #", "C. <!-- -->", "D. %"],
     "answer": "B"},

    {"question": "Which function is used to display output in Python?",
     "options": ["A. echo()", "B. print()", "C. write()", "D. show()"],
     "answer": "B"}
]

score = 0

print("Welcome to the Python Quiz!\n")

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {q['answer']}.\n")

print(f"Your final score is {score}/{len(questions)}")
