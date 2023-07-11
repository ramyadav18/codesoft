import random
quiz_data = {
    "Which Indian Captain holds the record for most test wins?": {
        "options": ["A. MS Dhoni", "B. Kapil Dev", "C. Ganguly", "D. Virat Kohli"],
        "answer": "D"
    },
    "Who is Known as Run Machine in Cricket?": {
        "options": ["A. Rohit Sharma", "B. Sachin Tendulkar", "C. Virat Kohli", "D. MS Dhoni"],
        "answer": "C"
    },
    "What is the Jersey number of Virat Kohli?": {
        "options": ["A. 45", "B. 18", "C. 7", "D. 10"],
        "answer": "B"
    },
    "Nick name of Virat Kohli?": {
        "options": ["A. Chiku", "B. Viru", "C. Kohli", "D. Raju"],
        "answer": "A"
    }
}
def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice questions.")
    print("Select the correct option (A, B, C, or D) for each question.")
    print("Let's see how well you know the topic!")

def present_quiz_questions():
    questions = list(quiz_data.keys())
    random.shuffle(questions)
    score = 0

    for question in questions:
        print("\n" + question)
        options = quiz_data[question]["options"]
        for option in options:
            print(option)
        user_answer = input("Your answer (A, B, C, or D): ").upper()

        if user_answer == quiz_data[question]["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print("The correct answer is:", quiz_data[question]["answer"])

    return score

def display_final_results(score):
    print("\nQuiz completed!")
    print("Your score:", score, "/", len(quiz_data))
    if score == len(quiz_data):
        print("Excellent! You answered all the questions correctly.")
    elif score >= len(quiz_data) // 2:
        print("Good job! You did well.")
    else:
        print("Keep practicing. You can do better!")

def play_quiz_game():
    display_welcome_message()
    score = present_quiz_questions()
    display_final_results(score)

    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_quiz_game()
    else:
        print("Thank you for playing the Quiz Game!")

play_quiz_game()
