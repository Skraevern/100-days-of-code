class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.correct_answers = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        user_answer = input(
            f"Q.{self.question_number + 1}: {question.text} (True/False)? "
        ).title()
        self.check_answer(user_answer, question.answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, question_answer):
        if user_answer == question_answer:
            print("You got it right")
            self.correct_answers += 1
        else:
            print("That's wrong")
        print(
            f"The correct answer was {self.question_list[self.question_number].text}."
        )
        print(
            f"Your current score is: {self.correct_answers}/{self.question_number + 1}"
        )
        print("")
