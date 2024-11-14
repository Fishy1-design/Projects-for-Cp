# ProficiencyTest: Simple Quiz Game, Elisheva Kibbie

import random

# Questions about goldfish, each with a diffrent difficulty rating from 1 to 10
questions = [
    {
        "question": "How long can goldfish live in captivity with proper care?",
        "options": ["10-20 years", "1-2 years", "5-6 months", "100 years", "5 years", "2 weeks"],
        "correct": "10-20 years",
        "difficulty": 5
    },
    {
        "question": "What is the ideal water temperature for goldfish?",
        "options": ["20-23°C", "5°C", "30°C", "10°C", "25°C", "0°C"],
        "correct": "20-23°C",
        "difficulty": 4
    },
    {
        "question": "Goldfish are a type of which animal?",
        "options": ["Fish", "Bird", "Mammal", "Reptile", "Amphibian", "Insect"],
        "correct": "Fish",
        "difficulty": 1
    },    
    {
        "question": "What is a common sign of a healthy goldfish?",
        "options": ["Active swimming", "Floating upside down", "Staying at the bottom", "Cloudy eyes", "Not eating", "Pale gills"],
        "correct": "Active swimming",
        "difficulty": 3
    },
    {
        "question": "How often should you change a portion of the water in a goldfish tank?",
        "options": ["Weekly", "Once a year", "Every hour", "Every day", "Every 6 months", "Monthly"],
        "correct": "Weekly",
        "difficulty": 4
    },
    {
        "question": "What do goldfish use to breathe?",
        "options": ["Gills", "Lungs", "Nose", "Skin pores", "Scales", "Tentacles"],
        "correct": "Gills",
        "difficulty": 2
    },
    {
        "question": "Which color change can goldfish undergo?",
        "options": ["Black to gold", "Blue to red", "Green to pink", "Yellow to purple", "Orange to blue", "Brown to silver"],
        "correct": "Black to gold",
        "difficulty": 6
    },
    {
        "question": "Goldfish belong to which family?",
        "options": ["Carp", "Salmon", "Shark", "Catfish", "Clownfish", "Eel"],
        "correct": "Carp",
        "difficulty": 3
    },
    {
        "question": "Goldfish have been bred for ornamental purposes since which dynasty?",
        "options": ["Song Dynasty", "Roman Empire", "Ming Dynasty", "Victorian Era", "Medieval Times", "Byzantine Empire"],
        "correct": "Song Dynasty",
        "difficulty": 9
    },
    {
        "question": "Can goldfish see more colors than humans?",
        "options": ["Yes, they can see infrared and ultraviolet light", "No, they are colorblind", "They only see black and white", "They can see in 3D", "They can see only green", "They are nocturnal"],
        "correct": "Yes, they can see infrared and ultraviolet light",
        "difficulty": 7
    },
    {
        "question": "What kind of water conditions do goldfish prefer?",
        "options": ["Clean and filtered", "Salty water", "Very warm water", "Stagnant water", "Acidic water", "Cold water"],
        "correct": "Clean and filtered",
        "difficulty": 4
    }
]

def get_random_question(current_difficulty):
    # This tells the program if the user got it wrong to give them a simpler question. 
    filtered_questions = [q for q in questions if q['difficulty'] <= current_difficulty]
    return random.choice(filtered_questions) if filtered_questions else None

def play_quiz():
    score = 0
    current_difficulty = 5  # The program starts with a Medium diffculty🦈
    while True:
        question = get_random_question(current_difficulty)
        if not question:
            print("No more questions available.")
            break

        print(f"\nQuestion: {question['question']}") #I'm mixing up the question order so its harder to guess so its harder every time, why? becuase im mean┗|｀O′|┛
        options = question["options"] # to-do: only pick four anwers for a question
        random.shuffle(options)
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")

        try:
            answer = int(input("Choose the number of your answer (1-6): ")) - 1 #This line asks th user to 
            if 0 <= answer < len(options):
                if options[answer] == question["correct"]:
                    print("Correct!")
                    score += 1
                    print(score)
                    current_difficulty = min(10, current_difficulty + 1)  # This causes the program to Increase the difficulty if the person got it right.
                else:
                    print(f"Incorrect! The correct answer was: {question['correct']}")
                    current_difficulty = max(1, current_difficulty - 1)  # This causes the program to Decrease the difficulty if the person got it right.
            else:
                print("Invalid choice. Please select a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        play_again = input("Do you want to continue? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_quiz()