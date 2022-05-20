# def add(*args):
#     soma=0
#     for n in args:
#         soma+=n
#     return soma

# print(add(2,6,9,5,13))

# def calculate(n, **kwargs):
#     n+= kwargs['add']
#     n*= kwargs['multiply']
#     return n
#     # total=0
#     # mult=1
#     # result=[]
#     # for k, v in kwargs.items():
#     #     if k== 'add':
#     #         total+=v
#     #     elif k=='multiply':
#     #         mult*=v
#     # result.append(mult)
#     # result.append(total)
#     # return result
# print(calculate(5, add=3, multiply= 5))
# class Car:
#     def __init__(self, **kw):
#         self.make= kw.get('make')
#         self.model= kw.get('model')

# my_car= Car(model='GT-R')
# print(my_car.make)
# print(my_car.model)
# def test(*args):
#     print(args)
#     print(type(args))
# test(1,3,6,4)

import tkinter


class NewWindow(tkinter.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title('E O NARGA?')
        self.minsize(width=512, height=512)
        self.bg= tkinter.PhotoImage(file='./Additional/narga.png')
        self.canvas1= tkinter.Canvas(self, width=500, height=300)
        self.canvas1.pack(fill='both', expand=True)
        self.canvas1.create_image(0,0, image= self.bg, anchor='nw')
        
        

window= tkinter.Tk() 
window.title('My First GUI Program')
window.minsize(width=400, height=500)
window.config(padx=100, pady=200)

#LABEL
my_label= tkinter.Label(text='I Am a Label', font=('Arial', 24, 'italic'))
my_label.config(padx=50, pady=50)

#BUTTON
def button_click():
    new_label= input.get()
    my_label.config(text= new_label)

btn= tkinter.Button(window, text='E O NARGA?', bd= '5', command=button_click)
btn2= tkinter.Button(window, text='NEW BUTTON', bd=5, command= window.destroy)

#ENTRY
input= tkinter.Entry()
input.insert(tkinter.END, string='Some text to begin with.')
#Get text in entry
# print(input.get())

#TEXT

text= tkinter.Text(height=5, width=30)
text.focus()
text.insert(tkinter.END, 'Example of multi-line text entry.')
#Get current value in textbox at line1, character 0
# print(text.get('1.0', tkinter.END))

#SPINBOX
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox= tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)

#SCALE
def scale_used(value):
    print(value)
scale= tkinter.Scale(from_=0, to=100, command=scale_used)

#CHECKBUTTON
def checkbutton_used():
    #prints 1 if On button checked, otherwise 0.
    print(checked_state.get()) 

#variable to hold on to checked state, 0 is off, 1 is on
checked_state= tkinter.IntVar()
checkbutton= tkinter.Checkbutton(text='IS ON?', variable=checked_state, command=checkbutton_used)
checked_state.get()

#RADIOBUTTON
def radio_used():
    print(radio_state.get())
#variable to hold on to wich radio button value is checked
radio_state= tkinter.IntVar()
radiobutton1= tkinter.Radiobutton(text='Option1', value=1, variable=radio_state, command=radio_used)
radiobutton2= tkinter.Radiobutton(text='Option2', value=2, variable=radio_state, command=radio_used)

#LISTBOX
def listbox_used(event):
    #Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox= tkinter.Listbox(height=4)
fruits= ['Apple', 'Pear', 'Orange', 'Banana']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind('<<ListboxSelect>>', listbox_used)
# listbox.pack(side='bottom')


#I CANT MIX PACK AND GRID
my_label.grid(column=0, row=0)
input.grid(column=3, row=2)
btn.grid(column=1, row=1)
btn2.grid(column=2, row=0)


# text.pack(expand=True)
# spinbox.pack(side='top')
# scale.pack(side='left')
# checkbutton.pack(side='right')
# radiobutton1.pack(side='bottom')
# radiobutton2.pack(side='bottom')


window.mainloop() 