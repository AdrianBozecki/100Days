class QuizBrain:
    def __init__(self, users_list):
        self.question_number = 0
        self.question_list = users_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, ans, correct_ans):
        if ans.lower() == correct_ans.lower():
            self.score += 1
            print(f"You got it right!")
        else:
            print(f"You're wrong")
        print(f"The correct answer was: {correct_ans}")
        print(f"Your current score is {self.score}/{self.question_number}.")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'\nQ.{self.question_number}: {current_question.text} (True/False): ')
        self.check_answer(user_answer, current_question.answer)


