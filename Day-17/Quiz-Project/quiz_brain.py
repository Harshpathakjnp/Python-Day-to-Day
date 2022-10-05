class QuizBrain:

    def __init__(self, q_list):
        self.score=0
        self.question_no = 0
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_no < len(self.question_list):
            return True
        return False

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_input = input(f"Q.{self.question_no}: {current_question.text} (True/False) : ")
        self.check_answer(user_input, current_question.answer)

    def check_answer(self, userinput, correctanswer):
        if userinput.lower() == correctanswer.lower():
            print("You got it Right !")
            self.score+=1
        else:
            print("You are Wrong !!")
        print(f"Your total Score is {self.score}/{self.question_no}\n")
