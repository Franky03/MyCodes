
from tkinter import *
from tkinter import messagebox
from letersandnumbers import letters, numbers, symbols
import random
import pyperclip
import json


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
        pass_input.config(show='')
    else:
        pass_input.config(show='*')


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    try:
        website= web_input.get()
        email= email_input.get()
        password= pass_input.get()
        new_data={website: {
        "email": email,
        'password': password
    }}

        # messagebox.showinfo(title='Title', message='Message')
        if len(password)==0 or len(website)==0 or len(email)==0:
            messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
        
        else:
            is_ok= messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email}\nPassword: {password}\n Is it ok to save?')

            if is_ok:
                try:
                    with open('./Udemy/PasswordGenerator/data.json','r') as file:
                        data= json.load(file)
                    
                except FileNotFoundError:
                    with open('./Udemy/PasswordGenerator/data.json', 'w') as file:
                        json.dump(new_data, file, indent=4)
                else:
                    data.update(new_data)

                    with open('./Udemy/PasswordGenerator/data.json', mode='w') as file:    
                        json.dump(data, file, indent=4)
                        
                finally:        
                    web_input.delete(0, END)
                    email_input.delete(0, END)
                    pass_input.delete(0, END)
                


    except:
        messagebox.showinfo(title='Oops', message='ERROR\nPlease Try Again.')
        
def search_web():
    website= web_input.get()
    try:
        with open('./Udemy/PasswordGenerator/data.json', mode='r') as file:
            data= json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Oops', message='No Data File Found.')
    else:
        if website in data:
            email= data[website]['email']
            password= data[website]['password']
            messagebox.showinfo(title=f'{website}', message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title='Oops', message=f'No details for {website} exists.')

    
        

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

web_input= Entry(width=32)
web_input.grid(row=1, column=1)
web_input.focus()
email_input= Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2)

pass_input= Entry(width=32, show='*')
pass_input.grid(row=3, column=1)

generate_btn= Button(text='Generate Password', command= generate)
generate_btn.grid(column=2, row=3)
add_btn= Button(text='Add', width=35, command=save)
add_btn.grid(column=1, row=5, columnspan=2)
search_btn= Button(text='Search', width=14, command=search_web)
search_btn.grid(row=1,column=2)

checked_state= IntVar()
checkbutton= Checkbutton(text='Show Password', variable=checked_state, command=show_passw)
checkbutton.grid(column=2, row=4)

window.mainloop()