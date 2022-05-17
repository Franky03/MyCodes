from resources import question_data

class Questions:
    def __init__(self, text, answer):
        self.text= text
        self.answer= answer
class Quiz:
    def __init__(self, list):
        self.quest_number= 0
        self.score= 0
        self.quest_list= list
    
    def still_has_quest(self):
        return self.quest_number < len(self.quest_list)
    
    def next_quest(self):
        current_quest= self.quest_list[self.quest_number]
        self.quest_number += 1
        user_answer= input(f'Q.{self.quest_number}: {current_quest.text} (True/False): ')
        self.check_answer(user_answer, current_quest.answer)
    
    def check_answer(self, user, correct):
        if user.lower() == correct.lower():
            self.score+=1 
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {answers[self.quest_number-1]}")
        print(f"Your current score is: {self.score}/{self.quest_number}")
        print("\n")
            

question_bank=[]
answers=[]
for question in question_data:
    question_text= question['question']
    quest_answer= question['correct_answer']
    answers.append(quest_answer)
    next_quest= Questions(question_text, quest_answer)
    question_bank.append(next_quest)
    
quiz= Quiz(question_bank)

while quiz.still_has_quest():
    quiz.next_quest()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.quest_number}")


