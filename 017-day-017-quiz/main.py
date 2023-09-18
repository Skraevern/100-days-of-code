from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os

os.system("cls||clear")

question_bank = []

for key in question_data:
    print(key)
category = input("Type in quiz category: ").title()

print(len(question_data[category]))

if category in question_data:
    for i in range(0, len(question_data[category])):
        question = Question(
            question_data[category][i]["question"],
            question_data[category][i]["correct_answer"],
        )
        question_bank.append(question)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz!")
    print(f"Your final score was: {quiz.correct_answers}/{quiz.question_number}")
else:
    print("Wrong input")
