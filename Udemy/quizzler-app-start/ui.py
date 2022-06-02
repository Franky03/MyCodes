from time import sleep
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.score=0
        self.quiz= quiz_brain

        self.window= Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas= Canvas(width=300, height=250, bg='white')
        self.quote= self.canvas.create_text(
            150,125,
            width=280,
            text='Text',
            fill=THEME_COLOR, 
            font=('Arial', 20, 'italic'))

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label= Label(text="Score: 0", fg='white', bg= THEME_COLOR, font=('Arial', 12, 'bold'))
        self.score_label.grid(row=0, column=1)

        self.true_img= PhotoImage(file="./Udemy/quizzler-app-start/images/true.png")
        self.true_btn= Button(image= self.true_img, highlightthickness=0, command= self.true_pressed)
        self.true_btn.grid(row=2, column=0)
        self.false_img= PhotoImage(file='./Udemy/quizzler-app-start/images/false.png')
        self.false_btn= Button(image= self.false_img, highlightthickness=0, command= self.false_pressed)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text= self.quiz.next_question()
            self.canvas.itemconfig(self.quote, text= q_text)
        else:
            self.canvas.itemconfig(self.quote, text="You've reached the end of the quiz.")
            self.true_btn.config(state='disable')
            self.false_btn.config(state='disable')
    
    def true_pressed(self):
        is_right= self.quiz.check_answer("True")
        self.feedback(is_right)
        
    def false_pressed(self):
        is_right= self.quiz.check_answer("False")
        self.feedback(is_right)
    
    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)


# self.score_label.config(text=f"Score: {self.quiz.score}")
#         self.canvas.config(bg='green')