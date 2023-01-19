from data import question_data
class Quiz:
    def __init__(self,q_list):
        self.q_numb=0
        self.q_list=q_list
        self.score=0

    def next_question(self):
        current_q=self.q_list[self.q_numb]
        n=input("Q" + str(self.q_numb+1) + ")" + current_q.text + "(True/False)?")
        self.q_numb+=1
        self.check_answer(n,current_q.answer)

    def still_has_questions(self):
        if self.q_numb==len(question_data):
            return False
        return True

    def check_answer(self,n,curr_ans):
        if(n.lower()==curr_ans.lower()):
            self.score+=1
            print("You got it right!!")
            print(f"Your score is {self.score}/{self.q_numb}")
            print()
        else:
            print(f"Thats wrong, the correct answer is {curr_ans} ")
            print(f"Your score is {self.score}/{self.q_numb}")
            print()

