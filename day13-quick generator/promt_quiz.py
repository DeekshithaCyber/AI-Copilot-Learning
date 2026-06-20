
score = 0
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. J.K. Rowling", "C. Ernest Hemingway", "D. Mark Twain"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"],
        "answer": "B"
    }
]
for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    user_answer = input("Your answer (A/B/C/D): ").upper()
    
    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is:", q["answer"])

print(f"\nQuiz completed! Your total score is: {score}/{len(questions)}")