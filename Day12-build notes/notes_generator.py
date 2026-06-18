notes = {
    "python": [
        "Python is easy to learn.",
        "Python supports OOP.",
        "Used in AI and Automation.",
        "Popular libraries are NumPy and Pandas."
    ],

    "cybersecurity": [
        "Protects systems and networks.",
        "CIA Triad: Confidentiality, Integrity, Availability.",
        "Learn networking basics.",
        "Understand common attacks."
    ],

    "linux": [
        "Linux is an open-source OS.",
        "Terminal is powerful.",
        "Learn basic commands.",
        "Used widely in servers."
    ]
}

topic = input("Enter a topic: ").lower()

if topic in notes:
    print(f"\nStudy Notes on {topic.title()}\n")

    for point in notes[topic]:
        print("-", point)

else:
    print("Notes not available for this topic.")