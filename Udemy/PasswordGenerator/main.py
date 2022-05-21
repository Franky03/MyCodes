from tkinter import *
from tkinter import messagebox
from letersandnumbers import letters, numbers, symbols
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    count()
    nmr_letters= random.randint(8,10)
    nmr_symbols= random.randint(2,4)
    nmr_numbers= random.randint(2,4)

    password_letters= [random.choice(letters) for _ in range(nmr_letters)]
    password_symbols=[random.choice(symbols) for _ in range(nmr_symbols)]
    numbers_symbols= [random.choice(numbers) for _ in range(nmr_numbers)]

    password_list= password_letters + password_symbols + numbers_symbols

    
    random.shuffle(password_list)
    password= "".join(password_list)
    pyperclip.copy(password)
    
    pass_input.insert(END, string= password)
    

alr= 0
def count():
    global alr
    alr+=1
    if alr>1:
        pass_input.delete(0, END)
        
def show_passw():
    if checked_state.get() == 1:
        pass_input.config(show='*')
    else:
        pass_input.config(show='')


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    try:
        website= web_input.get()
        email= email_input.get()
        password= pass_input.get()

        # messagebox.showinfo(title='Title', message='Message')
        if len(password)==0 or len(website)==0 or len(email)==0:
            messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
        
        else:
            is_ok= messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email}\nPassword: {password}\n Is it ok to save?')

            if is_ok:
                with open('./Udemy/PasswordGenerator/passwords.txt', mode='a+') as file:
                    file.write(f'{website} | {email} | {password}\n')
                    web_input.delete(0, END)
                    email_input.delete(0, END)
                    pass_input.delete(0, END)

    except:
        print('ERROR')
        

# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title('Password Manager')

window.config(padx=50, pady=50)
image= PhotoImage(file='./Udemy/PasswordGenerator/logo.png')
canvas= Canvas(width=200,height=200, highlightthickness=0)
canvas.create_image(100,100, image= image)
canvas.grid(column=1, row=0)

web_label= Label(text='Website:', font= ('Arial', 12))
web_label.grid(column=0, row=1)
email_label= Label(text='Email/Username:', font= ('Arial', 12))
email_label.grid(column=0, row=2)
pass_label= Label(text='Password:', font= ('Arial', 12))
pass_label.grid(column=0, row=3)

web_input= Entry(width=50)
web_input.grid(row=1, column=1, columnspan=2)
web_input.focus()
email_input= Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2)
# email_input.insert(END, 'kaikym20@gmail.com')
pass_input= Entry(width=32)
pass_input.grid(row=3, column=1)

generate_btn= Button(text='Generate Password', command= generate)
generate_btn.grid(column=2, row=3)
add_btn= Button(text='Add', width=35, command=save)
add_btn.grid(column=1, row=5, columnspan=2)

checked_state= IntVar()
checkbutton= Checkbutton(text='Show Password', variable=checked_state, command=show_passw)
checkbutton.grid(column=2, row=4)

window.mainloop()