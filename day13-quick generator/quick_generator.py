# quiz_generator.py

topic = input("Enter topic: ")

quiz = {
    "Python": [
        {
            "question": "What keyword is used to define a function?",
            "options": ["A. function", "B. define", "C. def", "D. fun"],
            "answer": "C. def"
        },
        {
            "question": "Which data type stores text?",
            "options": ["A. int", "B. str", "C. float", "D. bool"],
            "answer": "B. str"
        }
    ]
}

if topic in quiz:
    for q in quiz[topic]:
        print("\n" + q["question"])

        for option in q["options"]:
            print(option)

        print("Answer:", q["answer"])
else:
    print("Topic not found.")