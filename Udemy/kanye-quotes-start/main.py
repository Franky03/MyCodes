from tkinter import *
import requests


def get_quote():
    response= requests.get(url='https://api.kanye.rest/')
    quote= response.json()['quote']
    canvas.itemconfig(quote_text, text= quote)


window= Tk()
window.title('Kanye Says...')
window.config(padx=50, pady=50)

canvas= Canvas(width=300, height=414)
bg= PhotoImage(file="./Udemy/kanye-quotes-start/background.png")
canvas.create_image(150, 207, image= bg)
quote_text= canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill='white')
get_quote()
canvas.grid(row=0, column=0)

kanye= PhotoImage(file="./Udemy/kanye-quotes-start/kanye.png")
kanye_button= Button(image= kanye, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()

