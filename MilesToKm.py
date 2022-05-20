from tkinter import *

window= Tk()
window.title('Mile to Km Converter')

input= Entry()


input.grid(column=1, row=0)
input.insert(END, string='0')
label= Label(text='Miles', font=('Arial', 12, 'italic'))
label.grid(column=2, row=0)

label2= Label(text='is equal to', font=('Arial', 12, 'italic'))
label2.grid(column=0, row=1)

label3= Label(text='Km', font=('Arial', 12, 'italic'))
label3.grid(column=2, row=1)

label4= Label(text='0', font=('Arial', 12, 'italic'))
label4.grid(column=1, row=1)

def calc():
    km= int(input.get()) * 1.6
    label4.config(text= str(km))
btn= Button(window, text= 'Calculate', bd=3, command=calc)
btn.grid(column=1, row=2)
window.mainloop()