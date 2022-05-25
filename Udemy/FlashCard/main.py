from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
#FUNCTIONS
try:
    data= pd.read_csv('./Udemy/FlashCard/data/words_to_learn.csv')
except FileNotFoundError:
    data= pd.read_csv('./Udemy/FlashCard/data/french_words.csv')
data_dict= data.to_dict(orient="records")
current_card= {}

def next_card():
    global current_card, flip
    window.after_cancel(flip)
    current_card= random.choice(data_dict)
    canvas.itemconfig(word, text= current_card['French'], fill='black')
    canvas.itemconfig(idiom, text='French', fill='black')
    canvas.itemconfig(imagem, image= front)
    flip= window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(idiom,text='English', fill='white')
    canvas.itemconfig(word, text= current_card['English'], fill='white')
    canvas.itemconfig(imagem, image= back)

def is_know():
    data_dict.remove(current_card)
    print(len(data_dict))
    data= pd.DataFrame(data_dict)
    data.to_csv('./Udemy/FlashCard/data/words_to_learn.csv', index=False)

    next_card()

#GUI
window= Tk()
window.title('Flashy')
window.config(padx=58, pady=58, bg=BACKGROUND_COLOR)
flip= window.after(3000, flip_card)

front= PhotoImage(file='./Udemy/FlashCard/images/card_front.png')
back= PhotoImage(file='./Udemy/FlashCard/images/card_back.png')
canvas= Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
imagem= canvas.create_image(400,263, image= front)

idiom= canvas.create_text(400,150,text='Title', font=('Arial', 40, 'italic'))
word= canvas.create_text(400,263,text='Word', font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

right_image= PhotoImage(file='./Udemy/FlashCard/images/right.png')
right_button= Button(image=right_image, highlightthickness=0, command=is_know)
right_button.grid(row=1, column=1)

wrong_image= PhotoImage(file='./Udemy/FlashCard/images/wrong.png')
wrong_button= Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()

