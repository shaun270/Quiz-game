from question_model import Question
from data import question_data
from quiz_brain import Quiz
question_bank=[]
for i in range(len(question_data)):
    question=Question(question_data[i]["text"],question_data[i]["answer"])
    question_bank.append(question)

quiz=Quiz(question_bank)

is_on=True

while is_on:
    quiz.next_question()
    is_on=quiz.still_has_questions()
print()
print(f"You have completed the quiz\nYour final score is {quiz.score} out of {quiz.q_numb}")


